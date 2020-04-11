# To install boto, use commandline command:
    # $python3 -m pip install boto3
import boto3

ec2 = boto3.client('ec2')
# To get descriptions, including tags, of all ec2 resources.
# Refer to boto3 docs to see structure of the response.
response = ec2.describe_instances()

a_file = open("./output/all_instances.md", "w")
print(response)
a_file.write(' %s\n' % response)
a_file.close()


# Now make a dict of tags with each key
tag_dict = {}
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        nameTag = ''
        for tag in instance["Tags"]:
            # Check if the tag key is already in the tag dict.
            theKey = '%s' % tag['Key']
            theValue = '%s' % tag['Value']
            if theKey == 'name' or theKey == 'Name':
                nameTag = theValue
            if theKey in tag_dict:
                if theValue in tag_dict[theKey]:
                    # Add the current instance to the list for this value.
                    tag_dict[theKey][theValue]["Instances"].append(
                        {"NameTag": nameTag, "InstanceId": instance['InstanceId'], "PrivateIpAddress": instance["PrivateIpAddress"]})
                else:
                    tag_dict[theKey][theValue] = {"Instances": [
                        {"NameTag": nameTag, "InstanceId": instance['InstanceId'], "PrivateIpAddress": instance["PrivateIpAddress"]}]}
            else:
                # Add new tag key to the tag dict.
                tag_dict[theKey] = {theValue: {"Instances": [
                    {"NameTag": nameTag, "InstanceId": instance['InstanceId'], "PrivateIpAddress": instance["PrivateIpAddress"]}]}}
                # else:
                #

# Overwrites existing ("w").  To append would use "a"
a_file = open("./output/all_tags.md", "w")
a_file.write("# Tags Currently In Use\n")
# sorted_list = sorted(unsorted_list, key=str.casefold)
for tagKey in sorted(tag_dict.keys(), key=str.casefold):
    a_file.write("\n## %s\n" % tagKey)
    # for each value of the tag
    for valueText in sorted(tag_dict[tagKey].keys(), key=str.casefold):
        a_file.write('\n- "%s"\n' % valueText)
        for instance in sorted(tag_dict[tagKey][valueText]["Instances"], key=lambda k: k['NameTag']):
            a_file.write("  - %s (%s) [%s]\n" % (instance["InstanceId"],
                         instance["NameTag"], instance["PrivateIpAddress"]))
a_file.close()

# Overwrites existing ("w").  To append would use "a"
a_file = open("./output/name_and_description.md", "w")
a_file.write("# Tags Currently In Use\n")
# sorted_list = sorted(unsorted_list, key=str.casefold)
for tagKey in sorted(tag_dict.keys(), key=str.casefold):
    if tagKey == 'Description':
        a_file.write("\n## %s\n" % tagKey)
        # for each value of the tag
        for valueText in sorted(tag_dict[tagKey].keys(), key=str.casefold):
            a_file.write('\n- "%s"\n' % valueText)
            for instance in sorted(tag_dict[tagKey][valueText]["Instances"], key=lambda k: k['NameTag']):
                a_file.write("  - %s (%s) [%s]\n" % (instance["NameTag"], instance["InstanceId"], instance["PrivateIpAddress"]))
a_file.close()





# Overwrites existing ("w").  To append would use "a"
a_file=open("./output/names_and_descriptions.md", "w")
a_file.write("# Tags Currently In Use\n")
# sorted_list = sorted(unsorted_list, key=str.casefold)
for tagKey in sorted(tag_dict.keys(), key=str.casefold):
    a_file.write("\n## %s\n" % tagKey)
    # for each value of the tag
    for valueText in sorted(tag_dict[tagKey].keys(), key=str.casefold):
        a_file.write('\n- "%s"\n' % valueText)
        for instance in sorted(tag_dict[tagKey][valueText]["Instances"], key=lambda k: k['NameTag']):
            a_file.write("  - %s (%s) [%s]\n" % (instance["InstanceId"],
                         instance["NameTag"], instance["PrivateIpAddress"]))
a_file.close()



# Overwrites existing ("w").  To append would use "a"
a_file=open("./output/all_names.md", "w")
# sorted_list = sorted(unsorted_list, key=str.casefold)
for tagKey in sorted(tag_dict.keys(), key=str.casefold):
    # for each value of the tag
    if tagKey == "Name":
        for valueText in sorted(tag_dict[tagKey].keys(), key=str.casefold):
            a_file.write('## %s\n\n' % valueText)
            for instance in sorted(tag_dict[tagKey][valueText]["Instances"], key=lambda k: k['NameTag']):
                a_file.write("  [%s](https://console.aws.amazon.com/ec2/home?region=us-east-1#Instances:search=%s;sort=tag:Name)\n" %
                             (valueText, instance["InstanceId"]))
                a_file.write("  * %s (%s) [%s]\n\n" % (instance["InstanceId"],
                             instance["NameTag"], instance["PrivateIpAddress"]))


# Overwrites existing ("w").  To append would use "a"
a_file=open("./output/names_organized.md", "w")
# sorted_list = sorted(unsorted_list, key=str.casefold)
for tagKey in sorted(tag_dict.keys(), key=str.casefold):
    # for each value of the tag
    if tagKey == "Name":
        for valueText in sorted(tag_dict[tagKey].keys(), key=str.casefold):
            a_file.write('## %s\n\n' % valueText)
            for instance in sorted(tag_dict[tagKey][valueText]["Instances"], key=lambda k: k['NameTag']):
                a_file.write("  [%s](https://console.aws.amazon.com/ec2/home?region=us-east-1#Instances:search=%s;sort=tag:Name)\n" %
                             (valueText, instance["InstanceId"]))
                a_file.write("  * %s (%s) [%s]\n\n" % (instance["InstanceId"],
                             instance["NameTag"], instance["PrivateIpAddress"]))
                a_file.write(" %s" % (instance))

# Overwrites existing ("w").  To append would use "a"

# write all the windows machines only.
a_file=open("./output/windows.md", "w")
# sorted_list = sorted(unsorted_list, key=str.casefold)
for tagKey in sorted(tag_dict.keys(), key=str.casefold):
    # for each value of the tag
    if tagKey == "Name":
        for valueText in sorted(tag_dict[tagKey].keys(), key=str.casefold):
            for someinstance in sorted(tag_dict[tagKey][valueText]["Instances"], key=lambda k: k['NameTag']):
                aninstance=ec2.describe_instances(
                    InstanceIds=[instance["InstanceId"], ],)
                for reservation in aninstance['Reservations']:
                    for innerinstance in reservation['Instances']:
                        theTagDict = {}
                        for tag in innerinstance["Tags"]:
                                                



                            a_file.write("  [%s](https://console.aws.amazon.com/ec2/home?region=us-east-1#Instances:search=%s;sort=tag:Name)\n" % (
                                valueText, instance["InstanceId"]))
                            a_file.write('## %s\n\n' %
                                            innerinstance['Platform'])
                        a_file.write("  * %s (%s) [%s]\n\n" % (
                            instance["InstanceId"], instance["NameTag"], instance["PrivateIpAddress"]))
#                       a_file.write( " %s\n"% (innerinstance))

# Now make a dict of tags with each key
tag_dict = {}
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        nameTag = ''
        for tag in instance["Tags"]:
            # Check if the tag key is already in the tag dict.
            theKey = '%s' % tag['Key']
            theValue = '%s' % tag['Value']
            if theKey == 'name' or theKey == 'Name':
                nameTag = theValue
            if theKey in theTagDict:
                if theValue in theTagDict[theKey]:
                    # Add the current instance to the list for this value.
                    theTagDict[theKey][theValue]["Instances"].append(
                        {"NameTag": nameTag, "InstanceId": instance['InstanceId'], "PrivateIpAddress": instance["PrivateIpAddress"]})
                else:
                    theTagDict[theKey][theValue] = {"Instances": [
                        {"NameTag": nameTag, "InstanceId": instance['InstanceId'], "PrivateIpAddress": instance["PrivateIpAddress"]}]}
            else:
                # Add new tag key to the tag dict.
                theTagDict[theKey] = {theValue: {"Instances": [
                    {"NameTag": nameTag, "InstanceId": instance['InstanceId'], "PrivateIpAddress": instance["PrivateIpAddress"]}]}}
                # else:
                #

# newlist = sorted(list_to_be_sorted, key=lambda k: k['name'])
