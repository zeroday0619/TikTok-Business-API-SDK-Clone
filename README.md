# TikTok Business API SDK - Python

Comprehensive collection of client libraries that enable our developers to build software to integrate with Business API faster and in a more standardized way.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.1.3

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

Please refer to the "Integration with Python SDK" section in the [README.md](https://github.com/tiktok/tiktok-business-api-sdk/blob/main/README.md) under the root folder.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import business_api_client
from business_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = business_api_client.AdAcoApi(business_api_client.ApiClient(configuration))
access_token = 'access_token_example' # str | Authorized access token. For details, see [Authentication](https://ads.tiktok.com/marketing_api/docs?id=1738373164380162).
body = business_api_client.AdAcoBody() # AdAcoBody | Ad Aco update parameters. (optional)

try:
    # Create an ACO ad by uploading necessary ad creatives to the library. [Ad Aco Create](https://ads.tiktok.com/marketing_api/docs?id=1739473063234626)
    api_response = api_instance.ad_aco_create(access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdAcoApi->ad_aco_create: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://business-api.tiktok.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdAcoApi* | [**ad_aco_create**](docs/AdAcoApi.md#ad_aco_create) | **POST** /open_api/v1.3/ad/aco/create/ | Create an ACO ad by uploading necessary ad creatives to the library. [Ad Aco Create](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739473063234626)
*CreativeAssetApi* | [**creative_portfolio_create**](docs/CreativeAssetApi.md#creative_portfolio_create) | **POST** /open_api/v1.3/creative/portfolio/create/ | Create a portfolio [Portfolio create](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739091950439426)
*CatalogApi* | [**catalog_available_country_get**](docs/CatalogApi.md#catalog_available_country_get) | **GET** /open_api/v1.3/catalog/available_country/get/ | Get the countries and regions that ads for a catalog can be delivered to. [Catalog Available Country Get](https://business-api.tiktok.com/portal/docs?id&#x3D;1740491257516034)
*CatalogApi* | [**catalog_capitalize**](docs/CatalogApi.md#catalog_capitalize) | **POST** /open_api/v1.3/catalog/capitalize/ | Migrate catalogs under your ad account to your Business Center. [Catalog Capitalize](https://business-api.tiktok.com/portal/docs?id&#x3D;1740490222539778)
*CatalogApi* | [**catalog_create**](docs/CatalogApi.md#catalog_create) | **POST** /open_api/v1.3/catalog/create/ | Create a catalog by specifying information such as name, targeted locations, and currency. [Catalog Create](https://business-api.tiktok.com/portal/docs?id&#x3D;1740306481704961)
*CatalogApi* | [**catalog_delete**](docs/CatalogApi.md#catalog_delete) | **POST** /open_api/v1.3/catalog/delete/ | Delete a catalog. [Catalog Delete](https://business-api.tiktok.com/portal/docs?id&#x3D;1740310064588801)
*CatalogApi* | [**catalog_eventsource_bind**](docs/CatalogApi.md#catalog_eventsource_bind) | **POST** /open_api/v1.3/catalog/eventsource/bind/ | Bind app or website event sources to a catalog in a Business Center. [Catalog Eventsource Bind](https://business-api.tiktok.com/portal/docs?id&#x3D;1740492491200513)
*CatalogApi* | [**catalog_eventsource_bind_get**](docs/CatalogApi.md#catalog_eventsource_bind_get) | **GET** /open_api/v1.3/catalog/eventsource_bind/get/ | Get event source binding information. [Catalog Eventsource Bind Get](https://business-api.tiktok.com/portal/docs?id&#x3D;1740492531343362)
*CatalogApi* | [**catalog_eventsource_unbind**](docs/CatalogApi.md#catalog_eventsource_unbind) | **POST** /open_api/v1.3/catalog/eventsource/unbind/ | Unbind event sources from a catalog. [Catalog Eventsource Unbind](https://business-api.tiktok.com/portal/docs?id&#x3D;1740492512449538)
*CatalogApi* | [**catalog_feed_delete**](docs/CatalogApi.md#catalog_feed_delete) | **POST** /open_api/v1.3/catalog/feed/delete/ | Delete a feed. [Catalog Feed Delete](https://business-api.tiktok.com/portal/docs?id&#x3D;1740665210863617)
*CatalogApi* | [**catalog_feed_get**](docs/CatalogApi.md#catalog_feed_get) | **GET** /open_api/v1.3/catalog/feed/get/ | Get all feeds or a particular feed. [Catalog Feed Get](https://business-api.tiktok.com/portal/docs?id&#x3D;1740665183073281)
*CatalogApi* | [**catalog_get**](docs/CatalogApi.md#catalog_get) | **GET** /open_api/v1.3/catalog/get/ | Get all catalogs or a particular catalog. [Catalog Get](https://business-api.tiktok.com/portal/docs?id&#x3D;1740315452868610)
*CatalogApi* | [**catalog_lexicon_get**](docs/CatalogApi.md#catalog_lexicon_get) | **GET** /open_api/v1.3/catalog/lexicon/get/ | Get the lexicon for your catalog for use in ad texts. [Catalog Lexicon Get](https://business-api.tiktok.com/portal/docs?id&#x3D;1740488375815169)
*CatalogApi* | [**catalog_location_currency_get**](docs/CatalogApi.md#catalog_location_currency_get) | **GET** /open_api/v1.3/catalog/location_currency/get/ | Get supported locations and corresponding currencies for Catalog API. [Catalog Location Currency Get](https://business-api.tiktok.com/portal/docs?id&#x3D;1740491571747841)
*CatalogApi* | [**catalog_overview**](docs/CatalogApi.md#catalog_overview) | **GET** /open_api/v1.3/catalog/overview/ | Get the number of products in different audit statuses in a catalog. [Catalog Overview](https://business-api.tiktok.com/portal/docs?id&#x3D;1740492470201345)
*CatalogApi* | [**catalog_product_delete**](docs/CatalogApi.md#catalog_product_delete) | **POST** /open_api/v1.3/catalog/product/delete/ | Delete products in bulk. [Catalog Product Delete](https://business-api.tiktok.com/portal/docs?id&#x3D;1740562489236481)
*CatalogApi* | [**catalog_product_file**](docs/CatalogApi.md#catalog_product_file) | **POST** /open_api/v1.3/catalog/product/file/ | Upload products via file URL. [Catalog Product File](https://business-api.tiktok.com/portal/docs?id&#x3D;1740496787164161)
*CatalogApi* | [**catalog_set_product_get**](docs/CatalogApi.md#catalog_set_product_get) | **GET** /open_api/v1.3/catalog/set/product/get/ | Get products in a product set. [Catalog Set Product Get](https://business-api.tiktok.com/portal/docs?id&#x3D;1740571478441986)
*CatalogApi* | [**catalog_update**](docs/CatalogApi.md#catalog_update) | **POST** /open_api/v1.3/catalog/update/ | Use this endpoint to update the name of a catalog. The catalog must be under a Business Center. [Catalog Update](https://business-api.tiktok.com/portal/docs?id&#x3D;1740306544966657)

## Documentation For Models

 - [AdAcoBody](docs/AdAcoBody.md)
 - [AdAcoBodyAvatarIcon](docs/AdAcoBodyAvatarIcon.md)
 - [AdAcoBodyAvatarIconList](docs/AdAcoBodyAvatarIconList.md)
 - [AdAcoBodyCallToActionList](docs/AdAcoBodyCallToActionList.md)
 - [AdAcoBodyCardList](docs/AdAcoBodyCardList.md)
 - [AdAcoBodyCommonMaterial](docs/AdAcoBodyCommonMaterial.md)
 - [AdAcoBodyCommonMaterialTrackingInfo](docs/AdAcoBodyCommonMaterialTrackingInfo.md)
 - [AdAcoBodyDeeplinkList](docs/AdAcoBodyDeeplinkList.md)
 - [AdAcoBodyDisplayNameList](docs/AdAcoBodyDisplayNameList.md)
 - [AdAcoBodyLandingPageUrls](docs/AdAcoBodyLandingPageUrls.md)
 - [AdAcoBodyMediaInfo](docs/AdAcoBodyMediaInfo.md)
 - [AdAcoBodyMediaInfoImageInfo](docs/AdAcoBodyMediaInfoImageInfo.md)
 - [AdAcoBodyMediaInfoList](docs/AdAcoBodyMediaInfoList.md)
 - [AdAcoBodyMediaInfoVideoInfo](docs/AdAcoBodyMediaInfoVideoInfo.md)
 - [AdAcoBodyPageList](docs/AdAcoBodyPageList.md)
 - [AdAcoBodyTitleList](docs/AdAcoBodyTitleList.md)
 - [CatalogCapitalizeBody](docs/CatalogCapitalizeBody.md)
 - [CatalogCreateBody](docs/CatalogCreateBody.md)
 - [CatalogDeleteBody](docs/CatalogDeleteBody.md)
 - [CatalogUpdateBody](docs/CatalogUpdateBody.md)
 - [EventsourceBindBody](docs/EventsourceBindBody.md)
 - [EventsourceUnbindBody](docs/EventsourceUnbindBody.md)
 - [FeedDeleteBody](docs/FeedDeleteBody.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [catalogcreateCatalogConf](docs/catalogcreateCatalogConf.md)
 - [creativeportfoliocreateAdvancedAudioInfo](docs/creativeportfoliocreateAdvancedAudioInfo.md)
 - [creativeportfoliocreateAdvancedGestureIcon](docs/creativeportfoliocreateAdvancedGestureIcon.md)
 - [creativeportfoliocreateBadgeImageInfo](docs/creativeportfoliocreateBadgeImageInfo.md)
 - [creativeportfoliocreateBadgePosition](docs/creativeportfoliocreateBadgePosition.md)
 - [creativeportfoliocreatePortfolioContent](docs/creativeportfoliocreatePortfolioContent.md)
 - [creativeportfoliocreateStickerParam](docs/creativeportfoliocreateStickerParam.md)
 - [PortfolioCreateBody](docs/PortfolioCreateBody.md)
 - [ProductDeleteBody](docs/ProductDeleteBody.md)
 - [ProductFileBody](docs/ProductFileBody.md)

## Documentation For Authorization

 All endpoints do not require authorization.

