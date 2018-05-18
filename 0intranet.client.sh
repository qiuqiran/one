registry_ip=192.168.0.10

echo "$registry_ip  local.registry" >> /etc/hosts
echo '{ "insecure-registries":["local.registry:5000"] }' > /etc/docker/daemon.json
service docker restart
