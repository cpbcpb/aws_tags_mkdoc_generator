import boto3
client = boto3.client("elb")

# Save response from server to response variable
response = client.describe_load_balancers()
# Start writing to output file
a_file = open("./output/load_balancer_descriptions.md", "w")
# Write a title
a_file.write('# Load balancer descriptions for whatever your default aws account is n\n')
# Write an alphabetically sorted list, sorted by name of the load balancer.
for description in sorted(response['LoadBalancerDescriptions'],  key=lambda desc: desc['LoadBalancerName']):
    # Print the name of the load balancer
    a_file.write('##%s\n\n' % description['LoadBalancerName'] )
    #print a link to the loadbalancer in the aws console.
    


a_file.write('### Entire Response\n\n')
a_file.write(' %s\n' % response)
a_file.close()
print("It worked!")
