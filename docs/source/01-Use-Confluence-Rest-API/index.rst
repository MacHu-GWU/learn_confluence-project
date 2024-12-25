Use Confluence Rest API
==============================================================================


1. Create a new API token in your Atlassian account
------------------------------------------------------------------------------
- Follow the Instruction in this official document `Manage API tokens for your Atlassian account <https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/>`_


2. Use the API token to authenticate your requests
------------------------------------------------------------------------------
- Follow the Instruction in this official document `Authentication and authorization <https://developer.atlassian.com/cloud/confluence/rest/v2/intro/#auth>`_


3. Try the API by listing all the spaces
------------------------------------------------------------------------------
- Follow the API in `Get Spaces <https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space/#api-spaces-get>`_ Document.

.. literalinclude:: ./test_confluence_api.py
   :language: python
   :linenos:
