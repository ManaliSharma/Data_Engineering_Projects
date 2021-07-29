from create_infrastructure import config_parse_file, aws_client, check_cluster_creation,config_persist_cluster_infos, delete_cluster_resources, get_cluster_props,delete_iam_resource

def main():
    config_parse_file()

    redshift = aws_client('redshift', "us-east-1")
    iam = aws_client('iam', "us-east-1")
    if check_cluster_creation(redshift):
        print('available')
        delete_cluster_resources(redshift)
        delete_iam_resource(iam)
        print('New redshift cluster status: ')
        print(get_cluster_props(redshift))
    else:
        print('notyet')


if __name__ == '__main__':
    main()
