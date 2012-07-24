#!/bin/sh

role_list="admin Member"
tenant_list="t1 t2"
user_list="t1a t1m t2a t2m t1at2m t1mt2a t1wor t2wor"
password="Mirantis123"

role_id()
{
    echo $(keystone role-list | grep " $1 " | cut -d ' ' -f2)
}

tenant_id()
{
    echo $(keystone tenant-list | grep " $1 " | cut -d ' ' -f2)
}

user_id()
{
    echo $(keystone user-list | grep " $1 " | cut -d ' ' -f2)
}

if [ "$1" == "create" ]
then
    # Creating tenants
    for t in $tenant_list
    do
        keystone tenant-create --name $t
    done

    # creating users in tenant 
    keystone user-create --name t1a --tenant_id $(tenant_id t1)
    keystone user-create --name t1m --tenant_id $(tenant_id t1)
    keystone user-create --name t1at2m --tenant_id $(tenant_id t1)
    keystone user-create --name t1mt2a --tenant_id $(tenant_id t1)
    keystone user-create --name t2a --tenant_id $(tenant_id t2)
    keystone user-create --name t2m --tenant_id $(tenant_id t2)
    
    # creating users without specified roles
    keystone user-create --name t1wor --tenant_id $(tenant_id t1)
    keystone user-create --name t2wor --tenant_id $(tenant_id t2)

    # grant roles for users
    if [ "$2" == "--with-roles" ]
    then
        keystone user-role-add --user $(user_id t1a) --role $(role_id admin) --tenant_id $(tenant_id t1)
        keystone user-role-add --user $(user_id t1m) --role $(role_id Member) --tenant_id $(tenant_id t1)
        keystone user-role-add --user $(user_id t1at2m) --role $(role_id admin) --tenant_id $(tenant_id t1)
        keystone user-role-add --user $(user_id t1at2m) --role $(role_id Member) --tenant_id $(tenant_id t2)
        keystone user-role-add --user $(user_id t1mt2a) --role $(role_id Member) --tenant_id $(tenant_id t1)
        keystone user-role-add --user $(user_id t1mt2a) --role $(role_id admin) --tenant_id $(tenant_id t2)
        keystone user-role-add --user $(user_id t2a) --role $(role_id admin) --tenant_id $(tenant_id t2)
        keystone user-role-add --user $(user_id t2m) --role $(role_id Member) --tenant_id $(tenant_id t2)
    fi

    # setting up new password for all users
    for u in $user_list
    do
        keystone user-password-update --pass $password $(user_id $u)
    done
    
    keystone tenant-list
elif [ "$1" == "delete" ]
then
    for u in $user_list; do keystone user-delete $(user_id $u); done
    if [ "$2" == "--with-tenants" ]
    then
        for t in $tenant_list; do keystone tenant-delete $(tenant_id $t); done
    fi
else
    echo "Prepare users for testing mysql_backend"
    echo "Use: $0 <create [--with-roles] | delete [--with-tenants]>"
fi
