from datawagon.models import Organization, Trail
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class OrganizationSerializer(ModelSerializer):
    networks = SerializerMethodField("get_networks")

    class Meta:
        model = Organization
        fields = (
            "id",
            "zone",
            "title",
            "inn",
            "address",
            "count_net_devices",
            "count_addresses",
            "networks",
        )

    def get_networks(self, organization: Organization):
        return (
            network.subnet.with_prefixlen
            for network in organization._network_organization
        )


class TrailSerializer(ModelSerializer):
    class Meta:
        model = Trail
        fields = (
            "id",
            "domain_name",
            "source",
            "classification",
            "severity",
        )
