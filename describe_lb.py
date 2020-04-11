import boto3
client = boto3.client("elb")
client2 = boto3.client("elbv2")
# Save response from server to response variable
response = client.describe_load_balancers()
response2 = client2.describe_load_balancers()
# Start writing to output file
a_file = open("./output/load_balancer_descriptions.md", "w")
# Write a title
a_file.write('# Load balancer descriptions for whatever your default aws account is n\n')

a_file.write('## Classic\n')
# Write an alphabetically sorted list, sorted by name of the load balancer.
for description in sorted(response['LoadBalancerDescriptions'],  key=lambda desc: desc['LoadBalancerName']):
    # Print the name of the load balancer
    a_file.write('\n### %s\n\n' % description['LoadBalancerName'] )
    #print a link to the loadbalancer in the aws console.
    a_file.write("  [%s](https://console.aws.amazon.com/ec2/home?region=us-east-1#LoadBalancers:search=%s)\n\n" % (
            description['LoadBalancerName'], description['LoadBalancerName']))
    for instance in description['Instances']:
        a_file.write('"InstanceId" :  [%s](https://console.aws.amazon.com/ec2/home?region=us-east-1#Instances:search=%s;sort=tag:Name)\n\n' %
                             (instance['InstanceId'], instance['InstanceId']))
a_file.write('### Entire Response\n\n')

for description in sorted(response['LoadBalancerDescriptions'],  key=lambda desc: desc['LoadBalancerName']):
    # Print the name of the load balancer
    a_file.write('#### %s\n\n' % description['LoadBalancerName'] )
    for key in description:
        a_file.write('%s : %s\n\n' % (key, description[key]))

# # Applcation Load Balancers
# a_file.write('## Application Load Balancers\n\n')

for description in sorted(response2['LoadBalancers'],  key=lambda desc: desc['LoadBalancerName']):
    # Print the name of the load balancer
    a_file.write('\n### %s (%s load balancer)\n\n' % (description['LoadBalancerName'], description['Type'] ))
    #print a link to the loadbalancer in the aws console.
    a_file.write("  [%s](https://console.aws.amazon.com/ec2/home?region=us-east-1#LoadBalancers:search=%s)\n\n" % (description['LoadBalancerName'], description['LoadBalancerName']))
    listenerDescription = client2.describe_listeners(
        LoadBalancerArn=('%s' % description['LoadBalancerArn'])       
    )
    for alistener in listenerDescription['Listeners']:
        for action in alistener['DefaultActions']:
            if 'TargetGroupArn' in action:
                targetGroupHealth= client2.describe_target_health(
                    TargetGroupArn=action['TargetGroupArn']
                )
                for hdescription in targetGroupHealth['TargetHealthDescriptions']:
                    a_file.write('"InstanceId":  [%s](https://console.aws.amazon.com/ec2/home?region=us-east-1#Instances:search=%s;sort=tag:Name)\n\n' %
                             (hdescription['Target']['Id'], hdescription['Target']['Id']))
                targetGroupInfo = client2.describe_target_groups(
                    TargetGroupArns=[action['TargetGroupArn']]
                )

    # for key in description:
    #     a_file.write('%s : %s\n\n' % (key, description[key]))
# a_file.write('%sn\n' % response2)
a_file.close()
print("It worked!")
