![Pytest](https://github.com/lilt/lilt-python/workflows/Pytest/badge.svg)
# lilt-python
The Lilt REST API enables programmatic access to the full-range of Lilt backend services including:
  * Training of and translating with interactive, adaptive machine translation
  * Large-scale translation memory
  * The Lexicon (a large-scale termbase)
  * Programmatic control of the Lilt CAT environment
  * Translation memory synchronization

Requests and responses are in JSON format. The REST API only responds to HTTPS / SSL requests.
## Authentication
Requests are authenticated via REST API key, which requires the Business plan.

Requests are authenticated using [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Add your REST API key as both the `username` and `password`.

For development, you may also pass the REST API key via the `key` query parameter. This is less secure than HTTP Basic Auth, and is not recommended for production use.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v2.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://lilt.com/docs/api](https://lilt.com/docs/api)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/lilt/lilt-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/lilt/lilt-python.git`)

Then import the package:
```python
import lilt
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import lilt
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import lilt
from lilt.rest import ApiException
from pprint import pprint

configuration = lilt.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
configuration = lilt.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://lilt.com/2
configuration.host = "https://lilt.com/2"
# Enter a context with an instance of the API client
with lilt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lilt.DocumentsApi(api_client)
    body = lilt.DocumentAssignmentParameters() # DocumentAssignmentParameters | 

    try:
        # Assign a Document
        api_response = api_instance.assign_document(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->assign_document: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://lilt.com/2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DocumentsApi* | [**assign_document**](docs/DocumentsApi.md#assign_document) | **PUT** /documents/share | Assign a Document
*DocumentsApi* | [**create_document**](docs/DocumentsApi.md#create_document) | **POST** /documents | Create a Document
*DocumentsApi* | [**delete_document**](docs/DocumentsApi.md#delete_document) | **DELETE** /documents | Delete a Document
*DocumentsApi* | [**download_file**](docs/DocumentsApi.md#download_file) | **GET** /documents/files | Download a File
*DocumentsApi* | [**get_document**](docs/DocumentsApi.md#get_document) | **GET** /documents | Retrieve a Document
*DocumentsApi* | [**pretranslate_document**](docs/DocumentsApi.md#pretranslate_document) | **POST** /documents/pretranslate | Pretranslate a Document
*DocumentsApi* | [**update_document**](docs/DocumentsApi.md#update_document) | **PUT** /documents | Update a Document
*DocumentsApi* | [**upload_document_file**](docs/DocumentsApi.md#upload_document_file) | **POST** /documents/files | Upload a File
*FilesApi* | [**delete_file**](docs/FilesApi.md#delete_file) | **DELETE** /files | Delete a File
*FilesApi* | [**get_files**](docs/FilesApi.md#get_files) | **GET** /files | Retrieve a File
*FilesApi* | [**upload_file**](docs/FilesApi.md#upload_file) | **POST** /files | Upload a File
*LanguagesApi* | [**get_languages**](docs/LanguagesApi.md#get_languages) | **GET** /languages | Retrieve supported languages
*LexiconApi* | [**query_lexicon**](docs/LexiconApi.md#query_lexicon) | **GET** /lexicon | Query a Lexicon
*LexiconApi* | [**update_lexicon**](docs/LexiconApi.md#update_lexicon) | **POST** /lexicon | Update a Lexicon
*MemoriesApi* | [**create_memory**](docs/MemoriesApi.md#create_memory) | **POST** /memories | Create a Memory
*MemoriesApi* | [**delete_memory**](docs/MemoriesApi.md#delete_memory) | **DELETE** /memories | Delete a Memory
*MemoriesApi* | [**get_memory**](docs/MemoriesApi.md#get_memory) | **GET** /memories | Retrieve a Memory
*MemoriesApi* | [**import_memory_file**](docs/MemoriesApi.md#import_memory_file) | **POST** /memories/import | File import for a Memory
*MemoriesApi* | [**query_memory**](docs/MemoriesApi.md#query_memory) | **GET** /memories/query | Query a Memory
*MemoriesApi* | [**sync_delete_memory**](docs/MemoriesApi.md#sync_delete_memory) | **DELETE** /memories/sync | Delete-sync for a Memory
*MemoriesApi* | [**sync_down_memory**](docs/MemoriesApi.md#sync_down_memory) | **GET** /memories/sync | Get-sync for a Memory
*MemoriesApi* | [**sync_insert_memory**](docs/MemoriesApi.md#sync_insert_memory) | **POST** /memories/sync | Insert-sync for a Memory
*MemoriesApi* | [**sync_update_memory**](docs/MemoriesApi.md#sync_update_memory) | **PUT** /memories/sync | Update-sync for a Memory
*MemoriesApi* | [**update_memory**](docs/MemoriesApi.md#update_memory) | **PUT** /memories | Update the name of a Memory
*ProjectsApi* | [**create_project**](docs/ProjectsApi.md#create_project) | **POST** /projects | Create a Project
*ProjectsApi* | [**delete_project**](docs/ProjectsApi.md#delete_project) | **DELETE** /projects | Delete a Project
*ProjectsApi* | [**get_project**](docs/ProjectsApi.md#get_project) | **GET** /projects | Retrieve a Project
*ProjectsApi* | [**get_project_report**](docs/ProjectsApi.md#get_project_report) | **GET** /projects/quote | Retrieve Project report
*ProjectsApi* | [**get_project_status**](docs/ProjectsApi.md#get_project_status) | **GET** /projects/status | Retrieve Project status
*ProjectsApi* | [**update_project**](docs/ProjectsApi.md#update_project) | **PUT** /projects | Update a Project
*QAApi* | [**qa_check**](docs/QAApi.md#qa_check) | **GET** /qa | Perform QA check
*RootApi* | [**root**](docs/RootApi.md#root) | **GET** / | Retrieve the REST API root
*SegmentsApi* | [**create_segment**](docs/SegmentsApi.md#create_segment) | **POST** /segments | Create a Segment
*SegmentsApi* | [**delete_segment**](docs/SegmentsApi.md#delete_segment) | **DELETE** /segments | Delete a Segment
*SegmentsApi* | [**get_segment**](docs/SegmentsApi.md#get_segment) | **GET** /segments | Retrieve a Segment
*SegmentsApi* | [**tag_segment**](docs/SegmentsApi.md#tag_segment) | **GET** /segments/tag | Tag a Segment
*SegmentsApi* | [**update_segment**](docs/SegmentsApi.md#update_segment) | **PUT** /segments | Update a Segment
*TranslateApi* | [**register_segment**](docs/TranslateApi.md#register_segment) | **GET** /translate/register | Register a segment
*TranslateApi* | [**translate_segment**](docs/TranslateApi.md#translate_segment) | **GET** /translate | Translate a segment


## Documentation For Models

 - [ApiRoot](docs/ApiRoot.md)
 - [DocumentAssignmentParameters](docs/DocumentAssignmentParameters.md)
 - [DocumentAssignmentResponse](docs/DocumentAssignmentResponse.md)
 - [DocumentDeleteResponse](docs/DocumentDeleteResponse.md)
 - [DocumentParameters](docs/DocumentParameters.md)
 - [DocumentPretranslateParameters](docs/DocumentPretranslateParameters.md)
 - [DocumentPretranslateResponse](docs/DocumentPretranslateResponse.md)
 - [DocumentPretranslating](docs/DocumentPretranslating.md)
 - [DocumentPretranslatingStatus](docs/DocumentPretranslatingStatus.md)
 - [DocumentUpdateParameters](docs/DocumentUpdateParameters.md)
 - [DocumentWithSegments](docs/DocumentWithSegments.md)
 - [DocumentWithoutSegments](docs/DocumentWithoutSegments.md)
 - [DocumentWithoutSegmentsStatus](docs/DocumentWithoutSegmentsStatus.md)
 - [Error](docs/Error.md)
 - [File](docs/File.md)
 - [FileResponse](docs/FileResponse.md)
 - [LanguagesResponse](docs/LanguagesResponse.md)
 - [LexiconEntry](docs/LexiconEntry.md)
 - [LexiconEntryExamples](docs/LexiconEntryExamples.md)
 - [LexiconEntrySourceSpan](docs/LexiconEntrySourceSpan.md)
 - [LexiconEntryTargetSpan](docs/LexiconEntryTargetSpan.md)
 - [LexiconEntryTranslations](docs/LexiconEntryTranslations.md)
 - [LexiconUpdateParameters](docs/LexiconUpdateParameters.md)
 - [LexiconUpdateResponse](docs/LexiconUpdateResponse.md)
 - [MatchBand](docs/MatchBand.md)
 - [Memory](docs/Memory.md)
 - [MemoryDeleteResponse](docs/MemoryDeleteResponse.md)
 - [MemoryImportResponse](docs/MemoryImportResponse.md)
 - [MemoryInsertResponse](docs/MemoryInsertResponse.md)
 - [MemoryParameters](docs/MemoryParameters.md)
 - [MemoryUpdateParameters](docs/MemoryUpdateParameters.md)
 - [MemoryUpdateResponse](docs/MemoryUpdateResponse.md)
 - [Project](docs/Project.md)
 - [ProjectDeleteResponse](docs/ProjectDeleteResponse.md)
 - [ProjectParameters](docs/ProjectParameters.md)
 - [ProjectQuote](docs/ProjectQuote.md)
 - [ProjectStatus](docs/ProjectStatus.md)
 - [ProjectUpdateResponse](docs/ProjectUpdateResponse.md)
 - [QARuleMatches](docs/QARuleMatches.md)
 - [QARuleMatchesContext](docs/QARuleMatchesContext.md)
 - [QARuleMatchesMatches](docs/QARuleMatchesMatches.md)
 - [QARuleMatchesReplacements](docs/QARuleMatchesReplacements.md)
 - [QARuleMatchesRule](docs/QARuleMatchesRule.md)
 - [QARuleMatchesRuleCategory](docs/QARuleMatchesRuleCategory.md)
 - [QARuleMatchesRuleUrls](docs/QARuleMatchesRuleUrls.md)
 - [ResourceStatus](docs/ResourceStatus.md)
 - [Segment](docs/Segment.md)
 - [SegmentDeleteResponse](docs/SegmentDeleteResponse.md)
 - [SegmentParameters](docs/SegmentParameters.md)
 - [SegmentUpdateParameters](docs/SegmentUpdateParameters.md)
 - [TaggedSegment](docs/TaggedSegment.md)
 - [TranslateRegisterResponse](docs/TranslateRegisterResponse.md)
 - [Translation](docs/Translation.md)
 - [TranslationList](docs/TranslationList.md)
 - [TranslationMemoryEntry](docs/TranslationMemoryEntry.md)


## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: key
- **Location**: URL query string


## BasicAuth

- **Type**: HTTP basic authentication


## Author

support@lilt.com


