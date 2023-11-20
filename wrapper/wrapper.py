from tapioca import TapiocaAdapter, JSONAdapterMixin,generate_wrapper_from_adapter

from .resource_mapping import RESOURCE_MAPPING
from .config import settings


class RessellerClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = settings.RESSELLERS_API_URL
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(RessellerClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        return params

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass

ResellersAdpter = generate_wrapper_from_adapter(RessellerClientAdapter)
