.. include:: ../common/common_definitions.rst
.. Included via wallet-instance-functionalities.rst at title level '=' (document title).


Wallet Instance Initialization and Registration
===============================================

This process allows the User who has just installed the Wallet Instance application to register the Wallet Instance with the Wallet Provider Backend. During this process, the Wallet Instance application will request a security and integrity assertion from the OS manufacturer, which also binds a long-lived key pair stored in a proper secure storage within the device itself. This assertion will be validated by the Wallet Provider, and if the validation is successful, the Wallet Provider will authenticate the Wallet Instance. For details see :ref:`mobile-application-instance:Mobile Application Instance Initialization`.

.. warning::
  During the registration phase of the Wallet Instance with the Wallet Provider it is also necessary to associate the Wallet Instance with a specific User, authenticating the User with the Wallet Provider. The authentication mechanism is at the discretion of the Wallet Provider and it will not be addressed within these guidelines, as each Wallet Provider may have its User authentication systems already implemented.

.. note::
  The Wallet Provider SHOULD associate the Wallet Instance (through the ``hardware_key_tag`` identifier) with a specific User uniquely identified within the Wallet Provider's systems. This will be useful for the lifecycle of the Wallet Instance and for a future revocation. For details see :ref:`mobile-application-instance:Mobile Application Instance`.


