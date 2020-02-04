# To install boto, use commandline command:
    # $python3 -m pip install boto3
import boto3
import json
# Make sure Amazon CLI is set up.
# Make sure desired AWS account is your default in your
# root .aws hidden config and credentials files.

ec2 = boto3.client('ec2')
# To get descriptions, including tags, of all ec2 resources.
# Refer to boto3 docs to see structure of the response.
response=ec2.describe_instances()

# Some hints about the structure of the response
# The response is a dict with a Reservations property.
    # Reservations is a dict with an Instances property.
        #  Instances is a list.
            # Each instance in Instances has an InstanceId.  
            # Instances do not repeat between Reservations.

# What Tag is storing the desired dependency data? Name it here.
doc_tag = "Dependencies"
# The user hasn't created this tag yet, so instead will make
# a helpful tool for user to see what instances still need
# tags, and what tags there are.

# Creating an all tags markdown file.  Will have all Tags,
# with a list values for each tag, and for each value
# the tagged instances.  Output example as follows

# # All Tags
#
# ## Tag Key 1
#
#    ### Tag Value 1
#
#            - #Instance_Id_1
#            - #Instance_Id_2
#    ### Tag Value 2
#
#            - #Instance_Id_3
#            - #Instance_Id_4

# first create a dict to organize the data to be written.
# tag_dict= {
#     'Tag_Key': {
#         'Tag_Value': {
#             'Instances':[instance_id_1, instance_id_2]
#             }
#         } 
#     }

# # just make a list of tags first
# tag_array=[]
# for reservation in response["Reservations"]:
#     for instance in reservation["Instances"]:
#         for tag in instance["Tags"]:
#             if tag['Key'] not in tag_array:
#                 tag_array.append(tag['Key'])
# print(tag_array)


# Now make a dict of tags with each key
tag_dict={}
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        nameTag=''
        for tag in instance["Tags"]:
            # Check if the tag key is already in the tag dict.
            theKey = '%s' % tag['Key']
            theValue = '%s' % tag['Value']
            if theKey == 'name' or theKey== 'Name':
                nameTag = theValue
            if theKey in tag_dict:
                if theValue in tag_dict[theKey]:
                    # Add the current instance to the list for this value.
                    tag_dict[theKey][theValue]["Instances"].append({"NameTag" : nameTag, "InstanceId": instance['InstanceId'] })
                else:
                    tag_dict[theKey][theValue] = {"Instances": [ {"NameTag" : nameTag, "InstanceId": instance['InstanceId'] }]}
            else:
                # Add new tag key to the tag dict.
                tag_dict[ theKey ]={ theValue: {"Instances": [ {"NameTag" : nameTag, "InstanceId": instance['InstanceId'] }]}}
                # else:
                #     

# Overwrites existing ("w").  To append would use "a"
a_file=open("./output/all_tags.md", "w")
a_file.write("# Tags Currently In Use\n\n")
# sorted_list = sorted(unsorted_list, key=str.casefold)
for tagKey in sorted(tag_dict.keys(), key=str.casefold):
    a_file.write("## %s\n\n" % tagKey)
    #for each value of the tag
    for valueText in sorted(tag_dict[tagKey].keys(), key=str.casefold):
        a_file.write("### %s\n\n" % valueText)
    # for key, value in tagValue:
    #     a_file.write("## %s\n\n\t" % key)
    #     for 
a_file.close()
