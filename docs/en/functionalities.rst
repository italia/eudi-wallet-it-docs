.. include:: ../common/common_definitions.rst
.. Included via index.rst at title level '=' (document title).


User Experience Design
=======================


.. include:: design.rst


Functionalities Overview
-------------------------

The IT-Wallet System provides Users with a simpler, faster, and more secure way to access services. This service is delivered through the use of a Wallet Solution, whose User Experience is structured into three main phases: pre-use, use, and post-use.

.. only:: format_html

  .. figure:: ./images/svg/UX-phases-usage.svg
    :alt: User Experience phases of Wallet usage
    :width: 100%
    :align: center

    User Experience phases of Wallet usage

.. only:: format_latex

  .. figure:: ./images/pdf/UX-phases-usage.pdf
    :alt: User Experience phases of Wallet usage
    :width: 100%
    :align: center

    User Experience phases of Wallet usage

The following sections focus on the usage and post-usage phases. They define the functional requirements supporting the User Experience for the activation, acquisition, presentation, management, and deactivation phases, along with interaction requirements related to error management, assistance requests, and feedback collection.

Additional documentation and resources are provided in the :ref:`official-resources:Official Resources` section.

The Official Resources include recommendations on the required User-Wallet Instance interactions and design best practices that promote consistency across different Wallet Solutions in terms of how functionalities are accessed and used.

To ensure a correct and consistent implementation, Primary Actors:

- MUST use the :ref:`official-resources:Official Resources` and MUST comply with all related usage specifications provided;

- MAY choose from the available configurations provided. Primary Actors MUST ensure the correct use of atomic components, such as the :ref:`functionalities:Engagement Button` or the :ref:`functionalities:Authentication Button`;

- MUST keep used resources up to date, in line with the latest available version of the :ref:`official-resources:Official Resources`.

Activation of the Wallet Instance
----------------------------------

Activation enables the User to access the Wallet Solution's functionalities for securely obtaining, presenting, and managing their Electronic Attestations. The activation process involves User Authentication with the Wallet Instance using their digital identity (see :ref:`wallet-instance-lifecycle:Wallet Instance Lifecycle`). After Authentication, the User obtains a person identification Attestation — either the EUDI **PID** or the national **IT-Wallet ID** — as described in :ref:`functionalities:Focus on Person Identification Attestations`.

Below are the User Experience requirements that the Wallet Provider MUST guarantee via their Wallet Solution:

- The User downloads the Wallet Solution onto their device to generate their Wallet Instance;
- The User sets an unlock PIN for their Wallet Instance if one has not been previously set in the app. In addition to the PIN, the User can decide to use their own unlock mechanism used within the device and managed at the operating system level (e.g., biometric authentication) as an alternative to the PIN. The User uses the unlock method whenever an authorization is required to ensure security and protect their information;
- The User reviews all relevant information regarding the activation process and service usage. Additionally, the User reads any policy from the Wallet Provider and from the issuer of the person identification Attestation (PID Provider or IT-Wallet ID provider) and/or the service's terms and conditions. The User gives their consent to proceed or declines to cancel the operation;
- The User selects an Authentication option from those available;
- The User completes the Authentication flow with the National Identity Provider's service;
- The User receives confirmation of the Authentication process outcome. If successful the User views a preview of the person identification Attestation (PID or IT-Wallet ID). The User confirms the previewed information to proceed, or cancels the operation;
- The User authorizes the operation using the unlock method previously set;
- The User receives confirmation of the successful activation of the Wallet Instance.

The Wallet Provider MUST allow the User to remove a person identification Attestation issued within the Authentication phase. In addition, the relevant issuer (PID Provider or IT-Wallet ID provider) SHOULD allow the User to revoke that Attestation through a specific Touchpoint. The Wallet Provider MUST allow the User to always have the option to request the deactivation of their Wallet Instance, even in the absence of the device on which it was installed. For further details, please refer to the :ref:`functionalities:Deactivation of the Wallet Instance` and :ref:`functionalities:Management of Electronic Attestations` sections.

In case of errors using the Wallet Instance, the Wallet Provider MUST guarantee that the User receives consistent messages that inform them and guide them toward resolving the issue. For further details, please refer to the :ref:`functionalities:Error Management` section.

The flow is shown below with illustrative wireframes.

.. only:: format_html

  .. figure:: ./images/svg/IT-Wallet-Activation-1.svg
    :alt: Example of User Experience in Activating a Wallet Instance
    :width: 100%
    :align: center

    Example of User Experience in Activating a Wallet Instance

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Wallet-Activation-01-1.pdf
    :alt: Example of User Experience in Activating a Wallet Instance
    :width: 100%

    Example of User Experience in Activating a Wallet Instance - 01

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Wallet-Activation-02-1.pdf
    :alt: Example of User Experience in Activating a Wallet Instance
    :width: 100%

    Example of User Experience in Activating a Wallet Instance - 02


Focus on Person Identification Attestations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section defines User Experience requirements for person identification Attestations held in the Wallet Instance: the EUDI **PID** and the national **IT-Wallet ID** (Electronic Attestation of Person Identification Data with national scope). Both convey a verified minimum set of information about the User identity (see :ref:`credential-data-model:Digital Credential Data Model`), but they differ in legal scope, issuer type, Wallet Instance lifecycle impact, and use cases for presentation supported.

Below are illustrated the User Experience requirements to ensure a uniform and consistent usage and display of the personal identification Attestation (PID and/or IT-Wallet ID). The Wallet Provider:

- MUST correctly display the person identification Attestation across all devices, ensuring a consistent experience on screens of varying sizes;
- MUST display the Attestation status if different from valid, to provide transparency on its lifecycle, and MAY display it if valid. Specific details about an invalid status MAY be provided (e.g., the reason why the Attestation was revoked);
- MUST include Action Buttons to enable lifecycle management of the Attestation and allow the User to revoke or update it at any time (see :ref:`functionalities:Management of Electronic Attestations`);
- MUST guarantee that the Attestation is a functional element for the User to be authenticated by a Relying Party in a digital context (see :ref:`functionalities:Authentication`), to access services in proximity contexts where applicable, and to request the issuance of additional EAAs where the related issuer requires person identification data (see :ref:`functionalities:Issuance of Electronic Attestations of Attributes`);
- MUST display a method of assistance provided by the relevant issuer of the Attestation (see :ref:`functionalities:User Assistance`);
- MUST guarantee that the Attestation is recognizable by the User and distinguishable from other EAAs.

PID
"""

The **PID** is the Person Identification Data under the European Digital Identity framework (see :ref:`credential-data-model-pid:PID Data Model` and :term:`Person Identification Data`). It is issued by the PID Provider as a technical PID (signed data structure) for presentation from the Wallet Instance.

- The Wallet Instance in the **Operational** state allows the PID issuance. Upon successful issuance of a valid PID, the Wallet Instance MUST transition to the **Valid** state (see :ref:`wallet-instance-lifecycle:Transition to Valid`).
- While the Wallet Instance is **Valid** and the PID is active/valid, the User MAY present the PID and use it for authentication and further credential issuance according to this specification and the EUDI framework.
- Revocation, expiry, or deletion of the PID MUST transition the Wallet Instance back to **Operational** (see :ref:`wallet-instance-lifecycle:Transition to Operational`).
- Where the User revokes the PID, the Wallet Provider MUST handle the consequences on the Wallet Instance lifecycle and on dependent EAAs as defined in this specification.
- The PID is intended for use also in cross-border interactions within the EUDI Wallet ecosystem, in addition to national use.

IT-Wallet ID
""""""""""""

The **IT-Wallet ID** is the Electronic Attestation of Person Identification Data with national scope, issued for national use only (see :ref:`credential-data-model-it-wallet-id:IT-Wallet ID Data Model` and :term:`IT-Wallet ID`). It is an EAA issued by an Electronic Attestation of Attributes Provider, unlike the PID.

- Issuance of the IT-Wallet ID does **not** transition the Wallet Instance to the **Valid** state; the Wallet Instance remains **Operational** (see :ref:`wallet-instance-lifecycle:Transition to Operational`).
- The IT-Wallet ID is exclusively intended for national use and not for cross-border interactions.
- To ensure a consistent identification and representation of the IT-Wallet ID across different Wallet Solutions, the Wallet Provider:

  - MUST use the official naming “IT-Wallet ID” in their Wallet Solutions;
  - MUST use the IT-Wallet ID official graphic asset available in the :ref:`official-resources:Official Resources` and MUST comply with the related usage specifications provided;
  - MUST use the IT-Wallet ID graphic asset in the ``application/svg+xml`` data format;
  - MUST NOT alter, modify, or replace the IT-Wallet ID graphic asset with unofficial graphic assets;
  - MUST maintain the minimum clear space as defined in the :ref:`official-resources:Official Resources` to ensure visibility and recognizability. No other graphic or textual elements MUST interfere with this space;
  - MUST NOT resize the IT-Wallet ID graphic asset below the minimum dimensions specified in the :ref:`official-resources:Official Resources` to maintain legibility across formats and devices;
  - MUST NOT place the IT-Wallet ID graphic asset on backgrounds that compromise its visibility or legibility. Adequate contrast between the IT-Wallet ID graphic asset and the background MUST be ensured, in line with the :ref:`official-resources:Official Resources`.

  Although the term IT-Wallet ID refers to the Electronic Attestation of Personal Identification Data, the IT-Wallet ID graphical asset MAY be used by the Wallet Provider to facilitate the User in identifying, more generally, their personal identification Attestations (IT-Wallet ID / PID).

.. only:: format_html

  .. figure:: ../../official_resources/IT-Wallet-ID/IT-Wallet-ID-Primary-BlueItalia.svg
    :alt: IT-Wallet ID official graphic asset on a light background
    :width: 100%
    :align: center

    IT-Wallet ID official graphic asset on a light background

.. only:: format_latex

  .. figure:: ./images/pdf/IT-Wallet-ID.pdf
    :alt: IT-Wallet ID official graphic asset on a light background
    :width: 100%

    IT-Wallet ID official graphic asset on a light background

The IT-Wallet ID Official Resource is provided in the related :ref:`official-resources:Official Resources` Section. Additional documentation on the IT-Wallet ID graphic asset is available in the Brand Manual, indicated in the :ref:`official-resources:Official Resources` section.


Issuance of Electronic Attestations of Attributes
--------------------------------------------------

Once activation is complete, the User MAY request and obtain one or more Electronic Attestations of Attributes within their Wallet Instance.

The Electronic Attestations of Attributes is a dynamic object that enables the User to demonstrate or certify in a reliable and verifiable manner, a condition, status or right, based on the information it contains. In particular, the Electronic Attestations of Attributes:

- **is defined by an Authentic Source**, the entity holding the source data;

- **consists of a set of Attributes**, the granular data that define it (no static images or PDFs), such as, for example, a characteristic (e.g. “resident”) or a status (e.g. “student”);

- **is issued by a Provider of Electronic Attestation of Attributes**, the entity that emits it on the basis of the information acquired and manages its lifecycle.

Depending on the User's specific needs, the type of Electronic Attestation of Attributes, and the offerings available from the Wallet Provider, the Electronic Attestation of Attributes Provider, and the Authentic Source, the request of Electronic Attestations of Attributes can occur in two ways:

- **from the Wallet Instance Catalog**: the User explores the list of Electronic Attestations of Attributes provided by the Wallet Solution, selects the one of interest, and initiates the request process, concluding with the issuance of the Electronic Attestation of Attributes in the Wallet Instance. This pathway is available for Credential types eligible for public discovery as determined by the Supervisory body policies during the onboarding process (see :ref:`registry:Digital Credentials Catalog`).

- **from a Touchpoint of the Authentic Source** (or the Electronic Attestation of Attributes Provider if it coincides with the Authentic Source; (see :ref:`credential-issuance-low-level:Credential Offer Flow`): the User interacts with the digital service of the Authentic Source, allowing them to get a specific Electronic Attestation of Attributes in their Wallet Instance via an :ref:`functionalities:Engagement Button`.

Although the methods for initiating the request are different, the issuance flows share a similar structure and process.

Issuance from the Wallet Instance Catalog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Below are illustrated the User Experience requirements for the issuance of an Electronic Attribute Attestation from the Catalog that the Wallet Solution Provider MUST guarantee through their own Wallet Solution:

- The User accesses their Wallet Instance using the unlock method previously set;
- The User selects the Electronic Attestation of Attributes they wish to request from the available options in the Catalog;
- The User selects from which Electronic Attestation Provider they want to obtain the Electronic Attribute Attestation, if there is more than one;
- The User views any additional information on requirements and/or limitations related to obtaining the Electronic Attestation of Attributes from the Authentic Source;
- The User views their personal identification data, if required by the Authentic Source for the request of the Electronic Attestation of Attributes, the name of the related Electronic Attestation of Attributes Provider, and any related information policy. The User gives their consent to proceed, presenting the required data to the Electronic Attestation of Attributes Provider, or cancels the operation;
- The User views a preview of the Electronic Attestation of Attributes. The User confirms the data shown in the preview to proceed with the request or cancels the operation;
- The User authorizes the operation using the unlock method previously set;
- The User views the positive outcome of the request;
- The User views the details of the requested Electronic Attestation of Attributes, including: the data contained in it, the name of the Electronic Attestation of Attributes Provider who issued the Attestation, and the name of the Authentic Source;
- The User has access to all issued Electronic Attestations by navigating the Wallet Instance.

The Authentic Source MAY provide additional information related to an Electronic Attestation of Attributes. This information MUST be displayed by the Wallet Instance to the User, before initiating the process of issuing the Electronic Attestation of Attributes. In order to properly draft this informational content, the Authentic Source:

- MUST use clear language (e.g. avoid technical or complex terms), be concise (e.g. avoid excessively long or elaborate texts) and inclusive (e.g. avoid ability-based verbs), following the best practices for writing, language and tone of voice described in [REF_ACCESSIBILITY] and, in the case of public entities, in [GL_DESIGN];

- MUST adhere to the specific purpose of the text, communicating useful information to the User before engaging in the issuance process (e.g. listing prerequisites or stating limitations that could affect the successful outcome of the procedure);

- MUST ensure that the information is constantly updated;

- MUST include a title and text in which it MAY include references to external channels to direct Users to a procedure, explore a specific topic and/or open support requests.

Following is an example of informative text:

.. note::
  **Title:** Who may obtain the document
  **Text:** The digital version of [Document name] is available only to those who already hold the physical one. Please, make sure to have already obtained the corresponding physical document. For more details, [read more information] (URL).

For further information, please refer to the section :ref:`registry:Authentic Source Registry` (see ``data_capabilities.user_information`` parameter).

The Wallet Provider MUST allow the User to remove an Electronic Attestation of Attributes through their Wallet Instance at any moment. In case of absence of the device where the Wallet Instance was activated, the Wallet Provider MUST allow the User to deactivate the entire Wallet Instance through a specific Touchpoint. In addition, the Electronic Attestation of Attributes Providers SHOULD allow the User to revoke the issued Digital Credentials through specific Touchpoints. For more details, please refer to the :ref:`functionalities:Deactivation of the Wallet Instance` and :ref:`functionalities:Management of Electronic Attestations` sections.

In the event of communication issues between the systems of the Electronic Attestation of Attributes Provider and the Authentic Source, or if administrative or technical processes prevent the immediate issuance of the Electronic Attestation of Attributes, the actors involved MAY support a deferred issuance process. In this case the Wallet Provider MUST guarantee that:

- Upon reaching the final step of the process, the User visualizes a message prompting them to wait until the Electronic Attestation of Attributes can be issued.
- The User is informed by the Electronic Attestation of Attributes Provider once the Electronic Attestation of Attributes becomes available.

If the User encounters incorrect data in an already obtained or in-progress Electronic Attestation of Attributes, the Wallet Provider SHOULD guarantee the User appropriate assistance via their Wallet Instance. For more information, please refer to the :ref:`functionalities:User Assistance` section.

In case of errors using the Wallet Instance, the Wallet Provider MUST guarantee that the User receives consistent messages that inform them and guide them toward resolving the issue. For further details, please refer to the :ref:`functionalities:Error Management` section.

The flow is shown below with illustrative wireframes.

.. only:: format_html

  .. figure:: ./images/svg/Issuance-from-catalog-1.svg
    :alt: Example of User Experience in the issuance an Electronic Attestation of Attributes from Catalog
    :width: 100%
    :align: center

    Example of User Experience in the issuance an Electronic Attestation of Attributes from Catalog

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Issuance-from-catalog-01-1.pdf
    :alt: Example of User Experience in the issuance an Electronic Attestation of Attributes from Catalog
    :width: 100%
    :align: center

    Example of User Experience in the issuance an Electronic Attestation of Attributes from Catalog - 01

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Issuance-from-catalog-02-1.pdf
    :alt: Example of User Experience in the issuance an Electronic Attestation of Attributes from Catalog
    :width: 100%
    :align: center

    Example of User Experience in the issuance an Electronic Attestation of Attributes from Catalog - 02

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Issuance-from-catalog-03-1.pdf
    :alt: Example of User Experience in the issuance an Electronic Attestation of Attributes from Catalog
    :width: 100%
    :align: center

    Example of User Experience in the issuance an Electronic Attestation of Attributes from Catalog - 03

Issuance from a Touchpoint of the Authentic Source
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Below are illustrated the User Experience requirements for the issuance of an Electronic Attribute Attestation from a Touchpoint of the Authentic Source (also known as :ref:`credential-issuance-low-level:Credential Offer Flow`) that the Authentic Source MUST guarantee through their Touchpoint:

- The User interacts with the :ref:`functionalities:Engagement Button` clearly displayed in the Touchpoint interface;
- The User selects the Wallet Solution with which to proceed, through an interface that MUST follow the directions and functionalities described for the *Selection Page* in the :ref:`functionalities:Authentication` section;
- (*cross-device only*) the User scans the QR code that invokes the opening of their chosen Wallet Instance, through an interface that MUST follow the directions and functionalities described for the *QR Code Page* in the :ref:`functionalities:Authentication` section; alternatively the User can exit the flow.
- The User accesses their Wallet Instance using the unlock method previously set;
- The User views their personal identification data, if required for the request of the Electronic Attestation of Attributes, the name of the related Electronic Attestation of Attributes Provider, and any related information policy. The User gives their consent to proceed, presenting the required data to the Electronic Attestation of Attributes Provider, or cancels the operation;
- The User views any additional information on requirements and/or limitations related to obtaining the Electronic Attestation of Attributes;
- The User views a preview of the Electronic Attestation of Attributes. The User confirms the data shown in the preview to proceed with the request or cancels the operation;
- The User authorizes the operation using the unlock method previously set;
- The User views the positive outcome of the request;
- The User views the details of the requested Electronic Attestation of Attributes, including: the data contained in it, the name of the Electronic Attestation of Attributes Provider who issued the Attestation, and the names of the Authentic Sources.

In case of errors during the issuance of the Electronic Attestation of Attributes, the Authentic Source MUST guarantee that the User receives consistent messages that inform them and guide them toward resolving the issue. For further details, please refer to the :ref:`functionalities:Error Management` section.

The flow is shown below with illustrative wireframes.

.. only:: format_html

  .. figure:: ./images/svg/Issuance-from-Authentic-Source-1.svg
    :alt: Example of User Experience in the issuance of an Electronic Attestation of Attributes from the Authentic Source
    :width: 100%
    :align: center

    Example of the User Experience during the issuance of an Electronic Attestation of Attributes from the Authentic Source.

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Issuance-from-Authentic-Source-same-device-01-1.pdf
    :alt: Example of User Experience in the issuance of an Electronic Attestation of Attributes from the Authentic Source, same device - 01.
    :width: 100%
    :align: center

    Example of User Experience in the issuance of an Electronic Attestation of Attributes from the Authentic Source, same device - 01

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Issuance-from-Authentic-Source-same-device-02-1.pdf
    :alt: Example of User Experience in the issuance of an Electronic Attestation of Attributes from the Authentic Source, same device - 02.
    :width: 100%
    :align: center

    Example of User Experience in the issuance of an Electronic Attestation of Attributes from the Authentic Source, same device - 02

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Issuance-from-Authentic-Source-cross-device-01-1.pdf
    :alt: Example of User Experience in the issuance of an Electronic Attestation of Attributes from the Authentic Source, cross device - 01.
    :width: 100%
    :align: center

    Example of User Experience in the issuance of an Electronic Attestation of Attributes from the Authentic Source, cross device - 01


.. only:: format_latex

  .. figure:: ./images/pdf/A4-Issuance-from-Authentic-Source-cross-device-02-1.pdf
    :alt: Example of User Experience in the issuance of an Electronic Attestation of Attributes from the Authentic Source, cross device - 02.
    :width: 100%
    :align: center

    Example of User Experience in the issuance of an Electronic Attestation of Attributes from the Authentic Source, cross device - 02


.. only:: format_latex

  .. figure:: ./images/pdf/A4-Issuance-from-Authentic-Source-cross-device-03-1.pdf
    :alt: Example of User Experience in the issuance of an Electronic Attestation of Attributes from the Authentic Source, cross device - 03.
    :width: 100%
    :align: center

    Example of User Experience in the issuance of an Electronic Attestation of Attributes from the Authentic Source, cross device - 03

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Issuance-from-Authentic-Source-cross-device-04-1.pdf
    :alt: Example of User Experience in the issuance of an Electronic Attestation of Attributes from the Authentic Source, cross device - 04.
    :width: 100%
    :align: center

    Example of User Experience in the issuance of an Electronic Attestation of Attributes from the Authentic Source, cross device - 04

Following is represented for illustrative purposes the page with the :ref:`functionalities:Engagement Button`, together with the Selection Page and the QR Code Page with the interface elements and texts updated according to the :ref:`functionalities:Issuance from a Touchpoint of the Authentic Source` flow.

.. only:: format_html

  .. figure:: ./images/svg/Credential-offer-ENG.svg
    :alt: Illustrative page with Engagement Button, Selection page and QR code page for the credential offer
    :width: 100%
    :align: center

    Illustrative page with Engagement Button, Selection page and QR code page for the credential offer


.. only:: format_latex

  .. figure:: ./images/pdf/Credential-offer-ENG.pdf
    :alt: Illustrative page with Engagement Button, Selection page and QR code page for the credential offer
    :width: 100%

    Illustrative page with Engagement Button, Selection page and QR code page for the credential offer


Engagement Button
""""""""""""""""""

The Engagement Button is an interactive element of the interface that allows the USer to start a process, for example of Authentication ("Login with IT-Wallet"), of issuance of an Electronic Attestation ("Add to It-Wallet") or of remote presentation ("Verify with It-Wallet).

Relying Parties MAY make available the Engagement Button in their Touchpoint's page to allow the User to use their services through a Wallet Instance.

The Engagement Button:

- MUST be used exactly as outlined in the Official Resources and MUST NOT be redesigned ad hoc;

- MUST be used only in the shapes, colors and proportions defined and MUST NOT be altered, distorted, or hidden;

- MUST be responsive to all screen resolutions and MUST be integrated in the Discovery Page in order to meet minimum usability and accessibility requirements;

- MUST maintain a minimum distance from other elements (quiet zone) of at least 24px;

- MUST state in their label the action to be done followed by "IT-Wallet", for example "Login with IT-Wallet", "Add to IT-Wallet", "Verify with IT-Wallet";

- MAY be accompanied by text explaining the added value of performing that action using the IT-Wallet system.

- Actors wishing to integrate the Engagement Button into their Touchpoints MUST ensure that it is translated into other languages, at least English.

Below are some non-mandatory examples of Engagement Button labels:
- Login with IT-Wallet (see :ref:`functionalities:Authentication Button`)

- Add to IT-Wallet (see :ref:`functionalities:Issuance from a Touchpoint of the Authentic Source`)

- Verify with IT-wallet (see :ref:`functionalities:Remote Presentation`)


Focus on Electronic Attestations of Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Designing and implementing an Electronic Attestation of Attributes properly is essential to bring real value to the entire system. In this regard, the role of the Authentic Source and the Wallet Provider is crucial.

- The Authentic Source is responsible for designing all the core features of the Electronic Attestation of Attributes in terms of:

 - **opportunity and perceived value**: what the EAA can attest, in which contexts of use and by whom;
 - **ease of understanding**: how simple and intuitive it is for those who use it and for those who verify it;
 - **communicative effectiveness**: how recognizable or reliable it is perceived to be by those who use or verify it.


- The Wallet Provider is responsible for presenting the Electronic Attestation of Attributes in accordance with:

 - the provisions set out in these Technical Specifications, with a view to ensuring system consistency and adherence to the principles of usability [GL_DESIGN] and accessibility [REF_ACCESSIBILITY];
 - the provisions of the Authentic Sources Registry and the Digital Credentials Catalog (see :ref:`registry:Registry Infrastructure`);
 - the UX/UI design of their Wallet Solution.

In order to guide the Authentic Source in designing and the Wallet Provider in accurately representing an EAA, below are the elements to be considered and the structure to be adopted at the Detail View level:

- **EAA name**, which is the official, distinctive and human-readable name of an EAA;

- **Identification Attributes** (if available), the User’s basic personal details in the following order:

 - Given name
 - Last name
 - Tax code
 - Date of birth
 - Place of birth
 - Etc.

- **Level I Attributes**, which are the data that represent and identify the specific type of EAA (e.g. driving licence number, category, expiry date, etc.)

- **Level II Attributes** (if available), which are detailed data used to describe or elaborate on a specific Level I Attribute. These Level II Attributes may be structured as:

 - **List of descriptions**, which is a list of values relating to the same object;
 - **List of Attributes with value**, which is a list of additional objects with associated values;

- **Metadata**, which are data identifying the details of the EAA at the level of:

 - **Authentic Source name**, which is the identifying name of the data owner or the official database holding the information behind the EAA, defined by the parameter ``data_capabilities.data_origin``;
 - **Provider of Electronic Attestation of Attributes name**, which is the identifying name of the entity that creates and issues the EAA, defined by the parameter ``organization_name``.

.. only:: format_html

  .. figure:: ./images/svg/Focus-EAA-I-II-Level-ENG.svg
    :alt: Example of Electronic Attestation of Attributes layout, Detail View
    :width: 100%
    :align: center

    Example of Electronic Attestation of Attributes layout, Detail View.

.. only:: format_latex

  .. figure:: ./images/pdf/A4-focus-EAA-I-II-Level-ENG.pdf
    :alt: Example of Electronic Attestation of Attributes layout, Detail View
    :width: 100%

    Example of Electronic Attestation of Attributes layout, Detail View.

Below are the detailed requirements for the design and the representation of EAA within the Wallet Solutions (see :ref:`registry:Authentic Source Registry` and :ref:`registry:Digital Credentials Catalog`). In particular:

The Authentic Source:

- MUST specify the **EAA name** using the ``credential_name`` parameter. In particular, the Authentic Source:

  - MUST use terms or phrases that correspond to or are similar to the name of any pre-existing version of the document to which the EAA corresponds, so as to facilitate recognition by the User;
  - MUST use clear and simple terms, avoiding anglicisms, acronyms or technical terms where possible;
  - SHOULD define a short and concise name.

- MUST specify the data owner or data source name using the parameter ``data_capabilities.data_origin``. In particular, the Authentic Source:

  - MUST use the official name to ensure maximum recognisability and trust by the User;
  - MUST follow the structure “[Acronym] - [Name]” if it wishes to use an acronym alongside the full name (e.g. “ANIS - National Register of higher education”);
  - MAY follow the structure “[Primary entity acronym] - [Secondary entity name]” if it is useful to separate the acronym from the full name in order to add a further level of detail and enhance the recognisability and sense of reliability of the entity in charge (e.g. “MIT - General Directorate for Motor Vehicles”).

- MAY provide the **Authentic Source’s logo** in two versions, a compact version via the ``organization_info.logo_uri`` parameter and an extended version via the ``organization_info.logo_extended_uri`` parameter. In particular, the Authentic Source:

  - MUST provide the logo only in one of the following formats: ``image/png``, ``image/svg+xml``, or ``image/webp``;
  - MUST provide the logo in both a positive and a negative version, if available;
  - MUST provide the logo with a minimum size of 30 × 30 pixels and a maximum size of 60 x 60 pixels, in its compact version;
  - MUST provide the logo with an aspect ratio of 1:1, in its compact version;
  - MUST provide the logo which does not exceed the maximum file size of 80 KB, in its compact version;
  - MUST provide the logo with a minimum size of 200 × 30 pixels and a maximum size of 650 × 180 pixels, in its extended version;
  - MUST provide the logo which does not exceed the maximum file size of 150 KB, in its extended version.

- MAY provide a distinctive **EAA logo** via the ``data_capabilities.logo_uri`` parameter. In particular, the Authentic Source:

  - MUST provide the logo only in one of the following formats: ``image/png``, ``image/svg+xml``, or ``image/webp``;
  - MUST provide the logo in both a positive and a negative version, if available;
  - MUST provide the logo with a minimum size of 200 × 30 pixels and a maximum size of 650 × 180 pixels;
  - MUST provide the logo with a maximum file size of 150 KB.

- MAY define a distinctive **EAA color** to be associated with a specific EAA via the ``data_capabilities.background_color`` parameter. The aim is to characterise the EAA, making it recognisable to the User, particularly in cases where the intention is to give a new EAA a strong identity or to maintain consistency with a corresponding physical document (e.g., consider the italian driving licence and its distinctive pink colour). In particular, the Authentic Source:

  - MUST provide the background color only using one of the following color modes: HEX, HSB, RGB, sRGB, HSL, or HSV.

- MUST specify the desired **Attributes order** via the ``data_capabilities.available_claims.order`` parameter. In particular, the Authentic Source:

  - MUST order the data according to the default structure:

    - Identification Attributes (optional);
    - Level I Attributes;
    - Level II Attributes (optional);

  - MUST NOT exceed two levels of nesting in the organisation of attributes;
  - SHOULD NOT exceed a maximum of 15 Attributes per level;
  - SHOULD NOT exceed a maximum of 85 characters for Attribute values;
  - SHOULD NOT exceed a maximum of 181 characters for the value of each description in the case of Level II Attributes with a “list of descriptions”.

The Wallet Provider:

- MUST clearly and accessibly display the identifying **EAA name** as defined by the ``credential_name`` parameter within the :ref:`registry:Digital Credentials Catalog`;

- MUST clearly and accessibly display the **EAA Attributes**, respecting the predefined macro-structure of the Detail View, the division of Attributes into level I and level II (where available), and the data ordering as defined by the parameter ``data_capabilities.available_claims_order`` within the :ref:`registry:Authentic Source Registry`. In particular, the Wallet Provider:

  - MUST represent the EAA in accordance with the predefined structure:

    - EAA name;
    - Identification Attributes (optional);
    - Level I Attributes;
    - Level II Attributes (optional);
    - Metadata.

  - MUST include the **Authentic Source’s logo** and/or the specific **EAA logo** if provided by the Authentic Source through the :ref:`registry:Authentic Source Registry`;

  - MUST ensure the adoption of the **EAA color** defined by the Authentic Source, if specified within the :ref:`registry:Authentic Source Registry`, at the hue (H) level. The Wallet Provider MAY optimize saturation (S) and brightness (B) values to adapt the specific color to accessibility requirements and/or to the graphical design choices of its Wallet Solution. If the Authentic Source does not provide color specifications, the Wallet Provider is required to define and adopt its own default graphical choices.

The Wallet Provider is the ultimate responsible party for the visual presentation of the Electronic Attestation of Attributes within its Wallet Solutions. Therefore, to ensure a high level of accessibility [REF_ACCESSIBILITY] and usability [GL_DESIGN], further user experience requirements are set out below. In particular, the Wallet Provider:

- MUST correctly display the EAA across all devices, ensuring a consistent experience on screens of varying sizes;
- MAY display the EAAs issued in the form of cards stacked in a list in the Preview View, in line with approaches already used by other digital wallets in the market;
- MUST optimize the EAA layout in the Preview View for scalability and usability, especially when multiple EAAs are displayed on the same screen;
- MUST display clearly the name of the EAA, as defined within the Digital Credentials Catalog via the ``credential_name`` parameter (see :ref:`registry:Digital Credentials Catalog`), in both the Detail View and the Preview View;
- MUST display the EAA status, if different from valid to provide transparency on its lifecycle and MAY display it if valid, in both the Detail View and the Preview View. Specific details about the EAA status, if invalid, MAY be provided in the Detail View (e.g., the reason why the EAA is revoked);
- MAY include optional information to enhance the User Experience and the EAA recognizability, both in the Preview View and the Detail View, such as the logo and/or the color, as defined by the Authentic Source within the Authentic Source Registry (see :ref:`registry:Authentic Source Registry`);
- MUST include the same data of the Preview View in the Detail View and give a complete representation of all the other Attributes, following the order defined by the Authentic Source within the Authentic Source Registry (see :ref:`registry:Authentic Source Registry`); MAY include specific details in the Detail View, for example information about use case scenario or the reason for the invalid state of the EAA;
- MUST include Action Buttons in the Detail View to enable the EAA lifecycle management and allow the User to revoke or to update an EAA at any time (see :ref:`functionalities:Management of Electronic Attestations`);
- MUST guarantee that the EAA is a functional element, for the User to access services provided by Relying Parties in digital and proximity contexts (see :ref:`functionalities:Presentation of Electronic Attestations`);
- MUST display in the Detail View a method of assistance given by the Authentic Source via the ``data_capabilities.contacts`` parameter (see :ref:`functionalities:User Assistance` and see :ref:`registry:Authentic Source Registry`).

Below an example of Electronic Attestation of Attribute layout, in a Preview View, and Detail View.

.. only:: format_html

  .. figure:: ./images/svg/Focus-EAA.svg
    :alt: Example of Electronic Attestation of Attribute layout, Preview View, and Detail View
    :width: 100%
    :align: center

    Example of Electronic Attestation of Attribute layout, Preview View, and Detail View.

.. only:: format_latex

  .. figure:: ./images/pdf/A4-focus-EAA.pdf
    :alt: Example of Electronic Attestation of Attribute layout, Preview View, and Detail View
    :width: 100%

    Example of Electronic Attestation of Attribute layout, Preview View, and Detail View.


Presentation of Electronic Attestations
----------------------------------------

The presentation process allows the User to access a service or demonstrate ownership of certain data or their eligibility to perform a specific action. The presentation of Electronic Attestations and their subsequent verification involves interaction between the Wallet Instance, managed by the User, and a Relying Party Instance. Depending on the circumstances and context of the interaction, the following scenarios can be outlined:

- **Proximity Presentation**: the User presents their personal identification data and/or EAA data through the Wallet Instance, directly to a Verifier or to a device designated for in-person verification.

- **Remote Presentation**: the User presents their personal identification data and/or EAA data through the Wallet Instance, to a Relying Party configured for online verification, for instance, to Authenticate and access the services offered.

Regardless of the type of presentation, the Wallet Provider MUST allow the Wallet Instance to inform the User of the identity of the Relying Party. In case of a Relying Party Intermediary, the User MUST be informed of the intermediary’s involvement during the presentation request phase. The identity of the primary Relying Party MUST always be visible to the User and MUST NOT be replaced by that of the Relying Party Intermediary.

Proximity Presentation
^^^^^^^^^^^^^^^^^^^^^^^

Proximity presentation allows the User to present their personal identification data and/or EAA data via their Wallet Instance, using one of two methods:

- **Supervised mode**: the User presents their personal identification data and/or EAA data through the Wallet Instance to a Verifier (e.g., law enforcement officer, desk operator) equipped with a dedicated verification system (:ref:`relying-party-instance:Mobile Relying Party Instance`).

- **Unsupervised mode**: the User presents their personal identification data and/or EAA data through the Wallet Instance to a designated device (e.g., turnstile, totem) provided with a dedicated verification system (Embedded Relying Party Instance).

Below are the User Experience requirements related to both methods that the Wallet Provider MUST guarantee via their Wallet Solution.

**Supervised Mode**

- The User accesses their Wallet Instance using the unlock method previously set;
- The User navigates to the feature dedicated to QR Code generation;
- The User presents the generated QR Code to the Verifier acting on behalf of the Relying Party, who scans it using the designated verification app or system;
- The User reviews their requested personal identification data and/or EAA data, the name of the requesting Service Provider, and any related policy. The User decides whether to present any non-mandatory data (Selective Disclosure). The User provides consent to proceed or cancels the operation;
- The User authorizes the operation using the unlock method previously set;
- The User receives confirmation of the successful presentation.

In case of errors using the Wallet Instance, the Wallet Provider MUST guarantee that the User receives consistent messages that inform them and guide them toward resolving the issue. For further details, please refer to the :ref:`functionalities:Error Management` section.

**Unsupervised Mode**

- The User accesses their Wallet Instance using the unlock method previously set;
- The User navigates to the feature dedicated to QR Code generation;
- The User presents the generated QR Code to the designated device (e.g., a turnstile) of the Relying Party for scanning;
- The User reviews their requested personal identification data and/or EAA data, the name of the requesting Service Provider, and any related policy. The User decides whether to present any non-mandatory data (Selective Disclosure). The User provides consent to proceed or cancels the operation;
- The User authorizes the operation using the unlock method previously set;
- The User receives confirmation of the successful presentation.

In case of errors using the Wallet Instance, the Wallet Provider MUST guarantee that the User receives consistent messages that inform them and guide them toward resolving the issue. For further details, please refer to the :ref:`functionalities:Error Management` section.

The flow is shown below with illustrative wireframes.

.. only:: format_html

  .. figure:: ./images/svg/proximity-presentation-1.svg
    :alt: Example of User Experience in proximity presentation
    :width: 100%
    :align: center

    Example of User Experience in proximity presentation.

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Proximity-presentation-1.pdf
    :alt: Example of User Experience in proximity presentation
    :width: 100%
    :align: center

    Example of User Experience in proximity presentation.

Remote Presentation
^^^^^^^^^^^^^^^^^^^^

Remote presentation allows the User to present their personal identification data and/or EAA data by interacting with a Relying Party's Touchpoint through the designated :ref:`functionalities:Engagement Button`.

This presentation can occur in two different modes, depending on the type of device used to access the service:

- **Same-device mode**: when the User accesses an online digital service integrated with a special verification system (:ref:`relying-party-instance:Web Relying Party Instance`) using the same device which the Wallet Instance is installed on;
- **Cross-device mode**: when the User accesses a digital service integrated with a special verification system (:ref:`relying-party-instance:Web Relying Party Instance`) using a different device from the one which the Wallet Instance is installed on.

Below are the User Experience requirements related to both methods that the Wallet Provider MUST guarantee via their Wallet Solution.

**Same-Device Mode**

- The User clicks the :ref:`functionalities:Engagement Button` provided on the Relying Party's Touchpoint;
- The User selects the Wallet Solution to proceed with, through an interface that MUST follow the instructions and functionalities provided for the Selection Page described in the :ref:`functionalities:Authentication` section;
- The User accesses their Wallet Instance using the unlock method previously set;
- The User reviews the requested personal identification data and/or EAA data, the name of the requesting Relying Party, and any related policy. The User decides whether to present any non-mandatory data (Selective Disclosure). The User provides consent to proceed or cancels the operation;
- The User authorizes the operation using the unlock method previously set;
- The User receives confirmation of the successful presentation within the Wallet Instance;
- The User returns to the Relying Party's Touchpoint, where they see confirmation of the completed presentation.

In case of errors using the Wallet Instance, the Wallet Provider MUST guarantee that the User receives consistent messages that inform them and guide them toward resolving the issue. For further details, please refer to the :ref:`functionalities:Error Management` section.

The flow is shown below with illustrative wireframes.

.. only:: format_html

  .. figure:: ./images/svg/Remote-presentation-same-device-1.svg
    :alt: Example of User Experience in remote, same-device presentation
    :width: 100%
    :align: center

    Example of User Experience in remote, same-device presentation.

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Remote-presentation-same-device-01-1.pdf
    :alt: Example of User Experience in remote, same-device presentation - 01
    :width: 100%
    :align: center

    Example of User Experience in remote, same-device presentation  - 01

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Remote-presentation-same-device-02-1.pdf
    :alt: Example of User Experience in remote, same-device presentation - 02
    :width: 100%
    :align: center

    Example of User Experience in remote, same-device presentation  - 02

**Cross-Device Mode**

- The User clicks the :ref:`functionalities:Engagement Button` provided on the Touchpoint of the Relying Party while accessing the service from a different device than the one where the Wallet Instance is installed;
- The User selects the Wallet Solution to proceed with, through an interface that MUST follow the instructions and functionalities provided for the Selection Page described in the :ref:`functionalities:Authentication` section;
- The User scans the QR Code provided by the Relying Party using their Wallet Instance or the camera on their device; the QR code interface MUST follow the instructions and functionalities provided for the QR Code Page described in the :ref:`functionalities:Authentication` section;
- The User reviews the requested personal identification data and/or EAA data, the name of the requesting Relying Party, and any related policy. The User decides whether to present any non-mandatory data (Selective Disclosure). The User provides consent to proceed or cancels the operation;
- The User authorizes the operation using the unlock method previously set;
- The User receives confirmation of the successful presentation within the Wallet Instance;
- The User returns to the Relying Party's Touchpoint and views confirmation of the completed presentation.

In case of errors using the Wallet Instance, the Wallet Provider MUST guarantee that the User receives consistent messages that inform them and guide them toward resolving the issue. For further details, please refer to the :ref:`functionalities:Error Management` section.

The flow is shown below with illustrative wireframes.

.. only:: format_html

  .. figure:: ./images/svg/Remote-presentation-cross-device-1.svg
    :alt: Example of User Experience in remote, cross-device presentation
    :width: 100%
    :align: center

    Example of User Experience in remote, cross-device presentation.


.. only:: format_latex

  .. figure:: ./images/pdf/A4-Remote-presentation-cross-device-01-1.pdf
    :alt: Example of User Experience in remote, cross-device presentation - 01
    :width: 100%
    :align: center

    Example of User Experience in remote, cross-device presentation - 01

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Remote-presentation-cross-device-02-1.pdf
    :alt: Example of User Experience in remote, cross-device presentation - 02
    :width: 100%
    :align: center

    Example of User Experience in remote, cross-device presentation - 02

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Remote-presentation-cross-device-03-1.pdf
    :alt: Example of User Experience in remote, cross-device presentation - 03
    :width: 100%
    :align: center

    Example of User Experience in remote, cross-device presentation - 03

Following is represented for illustrative purposes the page with the :ref:`functionalities:Engagement Button`, together with the Selection Page, the QR Code Page and the Thank You Page with the interface elements and texts updated according to the :ref:`functionalities:Remote Presentation` flow.

.. only:: format_html

  .. figure:: ./images/svg/remote-presentation.svg
    :alt: Illustrative page with Engagement Button, Selection page, QR code page, Thank you page for the remote presentation
    :width: 100%
    :align: center

    Illustrative page with Engagement Button, Selection page, QR code page, Thank you page for the remote presentation


.. only:: format_latex

  .. figure:: ./images/pdf/remote-presentation-1.pdf
    :alt: Illustrative page with Engagement Button, Selection page, QR code page, Thank you page for the remote presentation
    :width: 100%

    Illustrative page with Engagement Button, Selection page, QR code page, Thank you page for the remote presentation

.. only:: format_latex

  .. figure:: ./images/pdf/remote-presentation-2.pdf
    :alt: Illustrative page with Engagement Button, Selection page, QR code page, Thank you page for the remote presentation
    :width: 100%

    Illustrative page with Engagement Button, Selection page, QR code page, Thank you page for the remote presentation


Authentication
"""""""""""""""

Authentication is a specific use case of remote presentation that allows the User to securely access services provided by both public and private Relying Parties. This is achieved by presenting their personal identification data and, if necessary, a set of Attributes contained in the obtained Electronic Attestations of Attributes. This process ensures that the User retains control over their data, including the ability to present only the information strictly necessary for verification by Relying Parties.

The Authentication process can be carried out using both the same-device and cross-device modes described above. For the User Experience functional requirements that MUST be addressed, please refer to the functional requirements for :ref:`remote presentation <functionalities:Remote Presentation>` in same-device and cross-device modes.

From a User Experience perspective, the Authentication process differs from the Presentation process only in how it is initiated, which is through a dedicated :ref:`functionalities:Authentication Button`.

To ensure a consistent and seamless Authentication process across all Relying Parties, each Relying Party MUST follow the visual and User Experience requirements outlined below, together with compliance with [REF_ACCESSIBILITY] and, in the case of public entities, with [GL_DESIGN].

Both flows are shown below with illustrative wireframes.

.. only:: format_html

  .. figure:: ./images/svg/Authentication-same-device-1.svg
    :alt: Example of same-device Authentication User Experience
    :width: 100%
    :align: center

    Example of same-device Authentication User Experience.

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Authentication-same-device-01-1.pdf
    :alt: Example of same-device Authentication User Experience - 01
    :width: 100%
    :align: center

    Example of same-device Authentication User Experience - 01

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Authentication-same-device-02-1.pdf
    :alt: Example of same-device Authentication User Experience - 02
    :width: 100%
    :align: center

    Example of same-device Authentication User Experience - 02

.. only:: format_html

  .. figure:: ./images/svg/Authentication-cross-device-1.svg
    :alt: Example of cross-device Authentication User Experience
    :width: 100%
    :align: center

    Example of cross-device Authentication User Experience.

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Authentication-cross-device-01-1.pdf
    :alt: Example of cross-device Authentication User Experience - 01
    :width: 100%
    :align: center

    Example of cross-device Authentication User Experience - 01

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Authentication-cross-device-02-1.pdf
    :alt: Example of cross-device Authentication User Experience - 02
    :width: 100%
    :align: center

    Example of cross-device Authentication User Experience - 02

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Authentication-cross-device-03-1.pdf
    :alt: Example of cross-device Authentication User Experience - 03
    :width: 100%
    :align: center

    Example of cross-device Authentication User Experience - 03

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Authentication-cross-device-04-1.pdf
    :alt: Example of cross-device Authentication User Experience - 04
    :width: 100%
    :align: center

    Example of cross-device Authentication User Experience - 04


Relying Parties SHOULD use the :ref:`official-resources:Official Resources` for design and development. If a Relying Party does not intend to use such open source resources, it MAY independently develop the Technical Solutions enabling the Authentication flow, ensuring that it follows the specifications herein provided.

.. note::
  The images in this section are to be considered illustrative as they are the subject of interface (UI) evolutions.

Relying Parties MUST implement and provide the following pages as part of the Authentication process:

- **Discovery Page**: lists all the available Authentication methods;
- **Selection Page**: shows the User all the Wallet Solutions available in the IT-Wallet System Register and let them choose which one to continue the Authentication process with;
- **QR Code Page** (*cross-device only*): prompts the User to scan a QR code;
- **Thank You Page**: confirms the successful Authentication;
- **Error Page**: displays error messages related to the Authentication process.

Each of these pages MUST include the following recurring elements, in line with the Visual Identity of the Relying Party's Touchpoint:

- A **header and/or subheader** allowing Users to navigate back to the previous page.
- A **footer** including the privacy policy, legal notice, and accessibility statement, where required by current regulations.

Specific requirements for each individual page are detailed below.

**Discovery Page**

To enable Authentication via the IT-Wallet System, the Relying Party MAY replace its existing Discovery Page with the version provided in the :ref:`official-resources:Official Resources`.

.. only:: format_html

  .. figure:: ./images/svg/discovery-page.svg
     :alt: Layout Model of Discovery Page in grid
     :width: 100%
     :align: center

     Layout Model of Discovery Page in grid

.. only:: format_latex

  .. figure:: ./images/pdf/discovery-page.pdf
     :alt: Layout Model of Discovery Page in grid
     :width: 100%

     Layout Model of Discovery Page in grid

Alternatively, the Relying Party MAY maintain its own Discovery Page but MUST integrate the Authentication Button as specified in the :ref:`functionalities:Authentication Button` section.

The Relying Party implementing the page:

- MUST display all available Digital Identity Authentication methods, including the IT-Wallet System Authentication through the Authentication Button;
- MAY also present alternative Authentication methods, if available;
- SHOULD provide essential supporting information to help the User make an informed and conscious choice.

If the User accesses the Discovery Page from a different Touchpoint than the one where the Wallet Instance is activated (cross-device), selecting IT-Wallet System Authentication MUST redirect the User to the QR Code Page.

If the User accesses the Discovery Page from the same Touchpoint where the Wallet Instance is activated (same-device), the selection MUST trigger the opening of the User's Wallet Instance.

**Selection Page**

The Selection Page is the page on which the User lands after they have chosen to Authenticate via the IT-Wallet System, and is intended to present the User with the Wallet Solutions available to perform Authentication.

.. note::
   This section describes the display of a Selection Page as part of the Authentication process use case. The same page SHOULD be used also by the Relying Parties during presentation and by third parties offering the Credential Offer to enable the Wallet Solution selection option. Further details are provided in :ref:`remote-flow:Remote Flow` and :ref:`credential-issuance-low-level:Credential Offer Flow`.


The Relying Party MUST implement the Selection Page made available in the :ref:`official-resources:Official Resources`.

.. only:: format_html

  .. figure:: ./images/svg/selection-page.svg
     :alt: Selection Page
     :width: 100%
     :align: center

     Selection Page

.. only:: format_latex

  .. figure:: ./images/pdf/selection-page-desktop-1.pdf
     :alt: Selection Page desktop
     :width: 100%

     Selection Page desktop

.. only:: format_latex

  .. figure:: ./images/pdf/selection-page-desktop-2.pdf
     :alt: Selection Page desktop
     :width: 100%

     Selection Page desktop

.. only:: format_latex

  .. figure:: ./images/pdf/selection-page-desktop-3.pdf
     :alt: Selection Page desktop
     :width: 100%

     Selection Page desktop

.. only:: format_latex

  .. figure:: ./images/pdf/selection-page-mobile.pdf
     :alt: Selection Page mobile
     :width: 100%

     Selection Page mobile

The Relying Party implementing the page:

- MUST include the elements proper to the Visual Identity of the IT-Wallet System, including the Logo by placing it alongside its own logo according to the guidance provided in the :ref:`brand-identity:Visual Identity` section;

- MUST ensure that the copy on the page mirrors that reported in the :ref:`official-resources:Official Resources`;

- MUST present each Wallet Solution in the IT-Wallet System Register through a modular component that displays the logo and name in full retrieved as described in :ref:`wallet-metadata-retrieval:Wallet Metadata Retrieval Flow`;

- MUST present the Wallet Solutions in a dynamic layout that adapts to the number of Wallet Solutions available: when the Wallet Solution number is less than 2, the Selection Page MUST distribute the Wallet Solutions within a center-column layout. Otherwise, when the Wallet Solution number is equal or superior than 3, the Selection Page MUST distribute the Wallet Solutions in a 2-column grid; in all cases random sorting MUST be guaranteed;

- MUST allow the User to search for a Wallet Solution through a filter feature by name, when more than 5 Wallet Solutions are present;

- MUST allow the User to find out, when needed, which Wallet Solutions are available in the IT-Wallet System Register by preparing a cross-reference to the official site of the IT-Wallet System;

- MUST include a Call to Action that allows the User to abort the operation and return to the previous page (e.g., the Discovery Page in case of an Authentication process).

The Relying Party MAY also include a text component on the Selection Page to promote the Authentication mode via IT-Wallet, which links back to the IT-Wallet System's official website, as represented in the :ref:`official-resources:Official Resources`.

**QR Code Page (cross-device only)**

The QR Code Page is presented to the User who selects IT-Wallet System Authentication within a cross-device process. Its purpose is to prompt the User to scan the generated QR code using their Wallet Instance or the camera of their device.

Relying Parties MUST implement the QR Code Page (cross-device) provided in the :ref:`official-resources:Official Resources`.

.. only:: format_html

  .. figure:: ./images/svg/QR-page.svg
     :alt: QR Code Page
     :width: 100%
     :align: center

     QR Code Page

.. only:: format_latex

  .. figure:: ./images/pdf/QR-page.pdf
     :alt: QR Code Page
     :width: 100%

     QR Code Page

The Relying Party implementing the page:

- MUST include the Visual Identity elements of the IT-Wallet System, including the logo;
- MUST ensure that the copy on the page mirrors that reported in the :ref:`official-resources:Official Resources`;
- MUST include a Call To Action allowing the User to generate a new QR code, if it has an expiration;
- MUST include a Call To Action allowing the User to cancel the operation and return to the Discovery Page.

Furthermore, in compliance with [REF_ACCESSIBILITY], regarding the QR code, the Relying Parties:

- MUST respect the minimum recommended dimensions to ensure effective scanning. A size of 150x150 pixels is generally adequate, but for codes with high data density (e.g. long URLs or numerous characters), it is advisable to increase it to 300x300 pixels or more;
- MUST ensure minimum contrast between the QR code and the background (the ideal condition provides for a white background with a black QR code);
- MUST avoid color inversions between background and QR code;
- MUST limit the presence to only one QR code per page;
- MUST ensure sharpness and high quality;
- MUST ensure SVG format;
- MUST ensure that it is not partially hidden by text or other elements.


**Thank You Page**

The Thank You Page is displayed after the User completes the Authentication process via their Wallet Instance. Its purpose is to inform the User about the successful Authentication.

Relying Parties MUST implement the Thank You Page provided in the :ref:`official-resources:Official Resources`.

.. only:: format_html

  .. figure:: ./images/svg/thank-you-page.svg
     :alt: Thank You Page
     :width: 100%
     :align: center

     Thank You Page

.. only:: format_latex

  .. figure:: ./images/pdf/thank-you-page.pdf
     :alt: Thank You Page
     :width: 100%

     Thank You Page

The Relying Party implementing the page:

- MUST include the Visual Identity elements of the IT-Wallet System, including the logo and an icon or graphical element consolidating the message;
- MUST ensure that the copy on the page mirrors that reported in the :ref:`official-resources:Official Resources`;
- MUST include a Call To Action prompting the User to proceed to the Touchpoint authenticated area.

**Error Page**

The Error Page is displayed when an issue occurs during the Authentication process. Its purpose is to inform the User about the nature of the error (e.g., technical issue, network issues, Wallet Instance malfunction, denied data sharing, etc.) and to present the available next steps. For further details, refer to the :ref:`functionalities:Error Management` section.

Relying Parties MUST implement the Error Page provided in the :ref:`official-resources:Official Resources`.

.. only:: format_html

  .. figure:: ./images/svg/error-page.svg
     :alt: Error Page
     :width: 100%
     :align: center

     Error Page

.. only:: format_latex

  .. figure:: ./images/pdf/error-page.pdf
     :alt: Error Page
     :width: 100%

     Error Page

The Relying Party implementing the page:

- MUST include the Visual Identity elements of the IT-Wallet System, including the logo and an icon or graphical element that conveys the type of error;
- MUST ensure that the copy on the page mirrors that reported in the :ref:`official-resources:Official Resources`;
- MUST include one or more Call To Action guiding the User toward the appropriate next step (e.g., retry, contact support, etc.).


Authentication Button
~~~~~~~~~~~~~~~~~~~~~~

The Authentication Button "Login with IT-Wallet" serves as an :ref:`functionalities:Engagement Button`, providing Users with a standardized way to Authenticate themselves using their digital Wallet.

Relying Parties MUST make the Authentication Button available within the Discovery Page of their Technical Solutions to allow the User to get authenticated into their services using the Wallet Instance under their control.

The Authentication Button has the following requirements:

- The Authentication Button MUST be used exactly as outlined in the :ref:`official-resources:Official Resources` and MUST NOT be redesigned ad hoc;

- The Authentication Button MUST be used only in the shapes, colors and proportions defined and MUST NOT be altered, distorted, or hidden;

- The Authentication Button MUST be responsive to all screen resolutions and MUST be integrated in the Discovery Page in order to meet minimum usability and accessibility requirements;

- Actors wishing to integrate the Authentication Button into their Technical Solution MUST ensure that it is translated into other languages, at least English;

- The Authentication Button MUST maintain a minimum distance from other elements (``quiet zone``) of at least 24px;

- The Authentication Button MUST state "Login with IT-Wallet";

- The Authentication Button SHOULD always be accompanied by an external link (e.g., "Learn more") that links to the official website of the IT-Wallet System, indicated in the :ref:`official-resources:Official Resources` section;

- Where space allows and/or the context requires it, the Authentication Button SHOULD be accompanied by a descriptive text: "IT-Wallet is the Italian digital wallet system that allows you to authenticate online and access public and private services quickly and securely, using the data, documents, and attestations you can obtain digitally in one of the participating wallets.".


Below are some non-mandatory examples of Authentication Button layout:


.. only:: format_html

  .. figure:: ./images/svg/authentication-button-layout.svg
     :alt: Variants of Authentication Button layout
     :width: 100%
     :align: center

     Variants of Authentication Button layout

.. only:: format_latex

  .. figure:: ./images/pdf/authentication-button-layout.pdf
     :alt: Variants of Authentication Button layout
     :width: 100%

     Variants of Authentication Button layout

The integration of the Authentication Button within the Discovery Page may vary depending on the page layout. Below are illustrative, non-exhaustive examples of Discovery Pages using grid, tab, and list layouts, respectively.

.. only:: format_html

  .. figure:: ./images/svg/discovery-page-layouts.svg
     :alt: Examples of Discovery Page layouts: grid, tab, and list
     :width: 100%
     :align: center

     Examples of Discovery Page layouts: grid, tab, and list

.. only:: format_latex

  .. figure:: ./images/pdf/discovery-page-layouts.pdf
     :alt: Examples of Discovery Page layouts: grid, tab, and list
     :width: 100%

     Examples of Discovery Page layouts: grid, tab, and list

For further details on the use of the Authentication Button, please refer to the :ref:`functionalities:Authentication` section.

**"Login with IT-Wallet" button - html code**

The button is available in three variants of dimensions (S - default / M / L) as per the .Italia Design System, and in "get" (call to an external page) and "post" (form inside the button) formats. In addition to the variants of dimensions, are provided two variants of button with fixed width, to be used in situations where it's preferable to keep consistency between similar buttons:

- the fixed-width version with icon on the left and centered text;
- the fixed‑width version with icon and text centered.

The Official Resource of the Authentication Button is available in the :ref:`official-resources:Official Resources` of these Technical Specification.

**"Login with IT-Wallet" button – svg**
For further information on the Authentication button refer to the Brand Manual, indicated in the :ref:`official-resources:Official Resources` section. The Authentication button Official Resource is available in the :ref:`official-resources:Official Resources` section of these Technical Specifications.

.. only:: format_html

  .. figure:: ../../official_resources/Authentication-button-ENG_size_variants.svg
     :alt: Authentication button in its dimension variants
     :width: 100%
     :align: center

     Example of Authentication button in its dimension variants

.. only:: format_latex

  .. figure:: ./images/pdf/Authentication-button.pdf
     :alt: Example of Authentication button in its dimension variants
     :width: 100%

     Example of Authentication button in its dimension variants


.. only:: format_html

  .. figure:: ../../official_resources/IT-Wallet-Authentication-Button/ENG/IT-Wallet-Authentication-Button-ENG-Fixed-Justified.svg
     :alt: Authentication button fixed justified
     :width: 100%
     :align: center

     Authentication button fixed justified

.. only:: format_latex

  .. figure:: ./images/pdf/Authentication-Button-ENG-Fixed-Justified.pdf
     :alt: Authentication Button fixed justified
     :width: 100%

     Authentication button fixed justified


.. only:: format_html

  .. figure:: ../../official_resources/IT-Wallet-Authentication-Button/ENG/IT-Wallet-Authentication-Button-ENG-Fixed-Centered.svg
     :alt: Authentication button fixed centered
     :width: 100%
     :align: center

     Authentication button fixed centered

.. only:: format_latex

  .. figure:: ./images/pdf/Authentication-Button-ENG-Fixed-Centered.pdf
     :alt: Authentication Button fixed centered
     :width: 100%

     Authentication button fixed centered


Management of Electronic Attestations
--------------------------------------

The Wallet Provider, via their Wallet Solution, and the PID provider or Electronic Attestations of Attributes Provider, via dedicated Touchpoints, MUST let the User manage their Electronic Attestations at any time.

This section outlines three different categories of requirements for managing each Electronic Attestations, specifically regarding:

- **Its status**: to allow the User to verify whether an Electronic Attestation is valid or invalid;
- **Its usage**: to enable the User to view and manage the history of presentations carried out with an Electronic Attestation;
- **Its data**: to allow the User to backup and restore each Electronic Attestation of Attributes in compliance with the principle of data portability.

Below are the key aspects that impact and define the User Experience in managing Electronic Attestations though the Wallet Instance, along with the functional requirements associated with each category.

Status of Electronic Attestations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To ensure reliability and promote the proper use of a Wallet Solution, the Wallet Provider MUST guarantee the User to always have visibility of the status of the Electronic Attestations issued within their Wallet Instance, based on the information received from the Electronic Attestations Provider, which manages their lifecycle.

The admissible statuses for an Electronic Attestation are as follows:

- **Valid** (``valid``): the EAA is issued without any evidence of criticalities or issues. In this case, the Wallet Instance MUST guarantee the User full presentation functionalities, both in proximity and remote scenarios;

- **Suspended** (``suspended``): the EAA is temporarily invalid, in a reversible condition (e.g., suspended driving license). In this case, the Wallet Instance:

  - MUST provide the User with adequate evidence of this status;
  - MUST invite the User to wait for the EAA to automatically return to a valid status at the end of the suspension period;
  - MUST guarantee the User presentation functionality, both in proximity and remote scenarios. Consequently, the Relying Party Instance MUST adequately inform the Verifier about the specific status of the EAA.

- **To be Updated** (``update`` or ``attribute_update``): the EAA is invalid because one or more of its information elements, at the metadata or Attribute level, is obsolete. In this case, the Wallet Instance:

  - If one or more of the EAA metadata is obsolete:

    - SHOULD automatically receive the EAA update managed by the Electronic Attestations Provider without informing or requiring action from the User or cause service interruptions in terms of EAA management and presentation.

  - If one or more of the EAA Attributes are obsolete:

    - MUST provide the User with adequate evidence;
    - MUST invite the User to update the EAA through a new issuance process;
    - MUST guarantee the User presentation functionality, both in proximity and remote scenarios. Consequently, the Relying Party Instance MUST adequately inform the Verifier about the specific status of the EAA.

- **Invalid** (``invalid``): the EAA is invalid, in an irreversible condition (e.g., revoked driving license). In this case, the Wallet Instance:

  - MUST provide the User with adequate evidence;
  - MUST invite the User to update or delete the EAA depending on whether they are entitled to re-obtain it and, therefore, use it again (e.g., a renewed driving license – which can be re-obtained as an EAA – or an exhausted medical prescription – which cannot be re-obtained as an EAA);
  - MUST guarantee the User presentation functionality, both in proximity and remote scenarios. Consequently, the Relying Party Instance MUST adequately inform the Verifier about the specific status of the EAA.

In addition to the statuses listed above, it should be specified that an EAA is subject to expiration. Two types of expiration are distinguished:

- **Administrative expiration**: characterizes certain EAAs and is provided by the Authentic Source within the Attributes of the EAA itself (e.g., driving license expiration date);
- **Technical expiration**: characterizes all EAAs and is defined by the Authentic Source in synergy with the Electronic Attestations Provider with the aim of mitigating security risks. This expiration is generally set at 1 year or, in any case, at a period less than or equal to the administrative expiration date.

Consequently, the EAA assumes the following additional statuses:

- **Expiring**: the EAA is valid but close to the administrative expiration date, if made available by the Authentic Source, or to the technical expiration. In this case, the Wallet Instance:

  - If the administrative expiration is approaching (e.g. 30 days remaining):

    - SHOULD provide the User with adequate evidence;
    - SHOULD invite the User to perform any necessary actions to re-obtain the updated EAA (e.g., renew the driving license at the competent offices);
    - MUST guarantee the User presentation functionality, both in proximity and remote scenarios.

  - If the technical expiration is approaching (e.g. 7 days remaining):

    - SHOULD automatically trigger the EAA update managed by the Electronic Attestations Provider without requiring action from the User.

    - If the automatic update is successful and returns an updated EAA:

     - MUST replace the previous one without resulting in unexpected duplicates, disruption or notification to the User;

    - If the automatic update is successful but does not return any EAA:

     - MUST provide the User with adequate evidence of the potential loss of entitlement to the EAA itself;
     - MUST invite the User to update or delete the EAA depending on whether they are entitled to re-obtain it and, therefore, use it again (e.g., a renewed driving license – which can be re-obtained as an EAA – or an exhausted medical prescription – which cannot be re-obtained as an EAA);
     - MUST guarantee the User presentation functionality, both in proximity and remote scenarios. Consequently, the Relying Party Instance MUST adequately inform the Verifier about the specific status of the EAA.

    - If the automatic update fails due to the service being unavailable or other technical errors:

     - SHOULD attempt the update at least once more before the EAA reaches its technical expiration date.

- **Expired**: the EAA is valid but has passed the administrative expiration date, if provided by the Authentic Source, or has passed the technical expiration date. In this case, the Wallet Instance:

  - If the administrative expiration date has passed:

    - MUST provide the User with adequate evidence;
    - MUST invite the User to perform any necessary actions to re-obtain the updated EAA (e.g., renew the license at the competent offices);
    - MUST guarantee the User presentation functionality, both in proximity and remote scenarios. Consequently, the Relying Party Instance MUST adequately inform the Verifier about the specific status of the EAA.

  - If the technical expiration date has passed (automatic update not performed or failed):

    - MUST provide the User with adequate evidence, distinguishing this specific case from an administrative expiration;
    - MUST invite the User to update the EAA by initiating an EAA re-issuance flow;
    - MUST allow the User presentation functionality, both in proximity and remote scenarios. Consequently, the Relying Party Instance MUST adequately inform the Verifier about the specific status of the EAA.

Below are the functional requirements supporting the User Experience regarding the update of the Electronic Attestation that the Electronic Attestation Provider MUST guarantee through the Wallet Solution:

- The User sees in the Electronic Attestation Preview View that its status is not valid;
- The User sees a message in the Detail View informing them of the new status of the Electronic Attestation and MAY find out more information;
- The User sees any additional information on the requirements and/or limitations relating to the status of the Electronic Attestation of Attributes and MAY close the message or proceed with any action requested by the Electronic Attestation Provider;
- The User sees specific Call To Action buttons in the Detail View to delete the Electronic Attestation or update it if no longer valid.

The flow is shown below with illustrative wireframes.

.. only:: format_html

  .. figure:: ./images/svg/Update-EAA.svg
     :alt: Example of User Experience in Updating an Electronic Attestation
     :width: 100%

     Example of User Experience in Updating an Electronic Attestation.

.. only:: format_latex

  .. figure:: ./images/pdf/A4-Update-EAA.pdf
    :alt: Example of User Experience in Updating an Electronic Attestation
    :width: 100%
    :align: center

    Example of User Experience in Updating an Electronic Attestation


Revocation of Electronic Attestations
""""""""""""""""""""""""""""""""""""""

Revocation is the procedure that turns an Electronic Attestation from a valid state to an invalid state. Revocation can occur in either an active or passive mode:

- **Active revocation**: This refers to the revocation of an Electronic Attestation at the User's request. This process affects only the Electronic Attestation and not its corresponding physical document, if one exists. Below is an illustrative list of scenarios in which the Wallet Provider MUST give the User the ability to request the revocation of an Electronic Attestation:

	- The User decides they no longer wish to use a specific Electronic Attestation;
	- The User decides to deactivate their Wallet Instance, thereby revoking all previously obtained Electronic Attestations;
	- The User no longer has possession of the device on which their Wallet Instance is installed due to loss or theft.

- **Passive revocation**: This refers to the revocation of an Electronic Attestation managed by the respective Electronic Attestation Provider on behalf of the Authentic Source. In this case, the Wallet Instance MUST inform the User of the status change of the Electronic Attestation and the Electronic Attestation Provider MAY additionally notify the User via other Touchpoints. Below is an illustrative list of scenarios that could lead to the revocation of an Electronic Attestation:

	- The physical document corresponding to the Electronic Attestation has been reported lost or damaged by the User through the appropriate channel/ Touchpoint;
	- The physical document corresponding to the Electronic Attestation has been revoked by the competent authorities;
	- The minimum security and/ or reliability requirements for one or more involved parties are no longer met.
	- The User's device no longer meets the minimum security requirements (rooted or jailbroken).

Below are the User Experience requirements that the Wallet Provider MUST guarantee via their Wallet Solution:
- The User opens the Detailed view of the Electronic Attestation that they want to revoke;
- The User selects the Call to Action to revoke the Electronic Attestation;
- The User reviews all information relevant to the action being performed and either gives their consent to proceed or denies consent to cancel the operation;
- The User sees the successful outcome of the revocation.

The flow is shown below with illustrative wireframes.

.. only:: format_html

  .. figure:: ./images/svg/Revocation-EAA-from-wallet-1.svg
     :alt: Example of User Experience in Revoking an Electronic Attestation
     :width: 100%
     :align: center

     Example of User Experience in Revoking an Electronic Attestation

     Example of User Experience in Revoking an Electronic Attestation.


.. only:: format_latex

  .. figure:: ./images/pdf/A4-Revocation-EAA-from-wallet-1.pdf
    :alt: Example of User Experience in Revoking an Electronic Attestation.
    :width: 100%
    :align: center

    Example of User Experience in Revoking an Electronic Attestation.

Transaction Logging
^^^^^^^^^^^^^^^^^^^
To ensure the principles of visibility and transparency, the Wallet Provider MUST provide a user-friendly dashboard in the Wallet Instance that allows the User to view the history of transactions performed using their Wallet Instance (e.g., Electronic Attestation issuance or presentation). In particular, the dashboard MUST:

- provide an overview of all recorded transactions and allow the User to access detailed views of individual transactions;
- enable the User, where a transaction involves a Relying Party, to easily initiate a data deletion request to the corresponding Relying Party (using logged contact information);
- support export of one or more transaction records to a file;
- allow the User to delete one or more transaction records with prior warning.

Backup and Restore of Electronic Attestation of Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the aim of ensuring the principle of data portability, the Wallet Solution MUST guarantee the User to have access to specific functionalities, particularly to:

- Request the backup and storage of Electronic Attestations of Attributes obtained through their Wallet Instance;
- Request the restore of their Electronic Attestations of Attributes on another Wallet Instance.

Deactivation of the Wallet Instance
------------------------------------

The deactivation of the Wallet Instance is the functionality that makes the Wallet Instance inactive and therefore no longer operational. The deactivation process can be triggered by different actors depending on the circumstances, specifically:

- By the User, in cases such as:

	- The device has been lost or stolen;
	- The device has been compromised;
	- The device has been reset to factory settings.

- By an authorized third party, in cases such as:

	- The Wallet Solution no longer meets the minimum security requirements.

The Wallet Provider MUST guarantee the User the ability to voluntarily deactivate their Wallet Instance through:

- The Wallet Instance itself;
- A Touchpoint (e.g., a website) provided by the Wallet Provider;
- The device's app store, by uninstalling the Wallet Instance.

Below are the functional and User Experience requirements that the Wallet Provider MUST guarantee via their Wallet Solution:

- The User accesses their Wallet Instance using the previously configured unlock method or Authenticates at the Touchpoint provided by the Wallet Provider;
- The User selects the Wallet Instance deactivation functionality;
- The User is informed that deactivating the Wallet Instance will invalidate previously obtained Electronic Attestations;
- The User confirms the action to proceed with deactivation, or cancels the operation;
- The User receives confirmation of successful deactivation;
- The User is notified that the Wallet Instance is inactive when logging in again.

The User has the ability to reactivate the Wallet Instance by re-downloading the app from the app store (if uninstalled) and/or by following the activation process again. For further details, please refer to the :ref:`functionalities:Activation of the Wallet Instance` section.

Once the Wallet Instance is reactivated, Electronic Attestations of Attributes can be re-obtained by starting the issuance or restore process again. For more details, please refer to sections :ref:`functionalities:Issuance of Electronic Attestations of Attributes` and :ref:`functionalities:Backup and Restore of Electronic Attestation of Attributes`.

In case of errors using the Wallet Instance, the Wallet Provider MUST guarantee that the User receives consistent messages that inform them and guide them toward resolving the issue. For more details, please refer to the :ref:`functionalities:Error Management` section.


The flow is shown below with illustrative wireframes.

.. only:: format_html

  .. figure:: ./images/svg/wallet-deactivation.svg
     :alt: Example of User Experience in Deactivating a Wallet Instance
     :width: 100%

     Example of User Experience in Deactivating a Wallet Instance.


.. only:: format_latex

  .. figure:: ./images/pdf/A4-wallet-deactivation.pdf
    :alt: Example of User Experience in Deactivating a Wallet Instance
    :width: 100%
    :align: center

    Example of User Experience in Deactivating a Wallet Instance

Error Management
-----------------

The IT-Wallet System involves the interaction of multiple services provided by different actors. It is therefore important to define an effective error management model with the goal of improving the perception and reliability of the entire ecosystem and enabling the User to feel guided during interactions with the various Technical Solutions and to consciously manage any issues while using the service.

Effective communication in case of an error also provides benefits for the actors involved, as it contributes to the reduction of assistance requests and, thus, to the minimisation of the impact on support systems.

Each Primary Actor MUST implement a proper error management, in compliance with current Technical Specification, in order to communicate errors and exceptions to the User and through the IT-Wallet Instance. Errors can be categorized, based on their nature, as follows:

- **The stage of the User Experience** where the error may occur: activation or deactivation of the Wallet Instance, obtaining, presenting, or managing Electronic Attestations of Attributes;
- **The type of error**: system error, communication error between actors, etc.;
- **The actor responsible** for the error: Wallet Provider, PID Provider, Electronic Attestations of Attributes Provider, Authentic Source;
- **The way the error is displayed**: message on the page, banner, toast message, and so on;
- **Suggested actions for the User** to resolve the error: suggestion to wait, request to try again, referral to FAQs and/or customer care, etc.;
- **The method for error management**: opening an assistance request through the Wallet Instance, linking to other detailed channels, and so on. For further details, please refer to the :ref:`functionalities:User Assistance` section.

Below is a non-exhaustive list of the main error cases, with reference to the actor responsible for their management, for each phase of the User Experience. The detailed list of errors to be managed for each interaction endpoint with the User is available in the dedicated error sections within :ref:`endpoints:Endpoints`.

Activation of the Wallet Instance Errors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :widths: 80 20
  :header-rows: 1

  * - **Error type**
    - **Actor in charge**
  * - The device does not support the Wallet Solution (e.g. absence of minimum security or technological requirements)
    - Wallet Provider
  * - The Wallet Provider's services are unresponsive (e.g. technical errors or lack of connection)
    - Wallet Provider
  * - The PID Provider or the IT-Wallet ID provider's services are unresponsive (e.g. technical errors)
    - PID Provider or IT-Wallet ID provider
  * - The Authentication process on the National Identity Provider's service was unsuccessful (e.g. technical errors, unrecognized identity, etc.)
    - National Identity Provider

.. note::
   When electronic document verification is performed in addition to National Identity Provider authentication, additional error scenarios may occur. For detailed error codes and handling procedures, see :ref:`credential-issuance-l2plus:Error Management`.

Issuance of Electronic Attestations of Attributes Errors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :widths: 80 20
  :header-rows: 1

  * - **Error type**
    - **Actor in charge**
  * -  The Wallet Instance and/or the PID / IT-Wallet ID are not valid
    - Wallet Instance
  * - The service for obtaining an Electronic Attestation of Attributes is unavailable (e.g. technical errors)
    - Electronic Attestations of Attributes Provider, Authentic Source
  * - The User is unable to obtain a specific Electronic Attestation of Attributes in their Wallet Instance (e.g. no eligibility, invalid or expired physical version, etc.)
    - Authentic Source
  * - The service for obtaining an Electronic Attestation of Attributes cannot be processed within the defined time interval
    - Electronic Attestations of Attributes Provider
  * - The service for obtaining an Electronic Attestation of Attributes cannot be completed synchronously. The User is requested to wait until the Attestation becomes available (deferred flow)
    - Electronic Attestations of Attributes Provider, Authentic Source
  * - The service for obtaining an Electronic Attestation of Attributes cannot be processed as the request exceeds the permitted limit (e.g. multiple Attestations requested at once)
    - Electronic Attestations of Attributes Provider

Presentation of Electronic Attestations Errors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :widths: 80 20
  :header-rows: 1

  * - **Error type**
    - **Actor in charge**
  * - The User does not hold the required Attributes contained in one or more Electronic Attestations within their Wallet Instance to access a specific service
    - Wallet Instance
  * - The Wallet Provider's services or the Relying Party's services are unresponsive (e.g. technical errors or lack of connection)
    - Wallet Provider, Relying Party

Management of Electronic Attestations Errors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :widths: 80 20
  :header-rows: 1

  * - **Error type**
    - **Actor in charge**
  * - The service for revocation/ backup/ restore of an Electronic Attestation of Attributes is unavailable (e.g. technical errors)
    - Electronic Attestations of Attributes Provider
  * - The service for revocation of PID is unavailable (e.g. technical errors)
    - PID Provider 
  * - The service for erasing information sent to a Relying Party is unavailable (e.g. technical errors)
    - Relying Party

Deactivation of the Wallet Instance Errors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :widths: 80 20
  :header-rows: 1

  * - **Error type**
    - **Actor in charge**
  * - The service for deactivating the Wallet Instance is unavailable (e.g. technical errors)
    - Wallet Provider

In addition to error management, all Primary Actors MUST also deal with negative feedback resulting from the User's decision to abandon or cancel a flow (e.g. Activation, Acquisition, Presentation, etc.). In such cases, feedback MUST be provided to confirm the User's choice, and it MAY include a Call to Action to continue.

User Assistance
----------------

For effective error management and the resolution of any other issues, Primary Actors MUST ensure adequate support to the User by structuring a simple and effective assistance model based on the following principles:

- **Self-resolution**: to allow the User to consult the frequently asked questions (FAQs) about the content and functionalities of the Wallet Instance, in order to resolve any error cases or issues independently.

- **Guided issue reporting**: to guide the User through the process of opening an assistance ticket, in order to clearly define the issue and facilitate its resolution.

- **Collaboration between actors**: to allow the coordination among each actor involved (Wallet Provider, Electronic Attestations of Attributes Provider, PID Provider, and Authentic Source), according to their specific roles and operational procedures.

- **Efficient communication**: to allow the User to track the updated status of their request throughout all stages of processing, with clear, continuous, and coordinated communication.

To apply these best practices, the involved actors SHOULD implement the following hierarchical support levels:

	1. **Level I | Self-management**: the Wallet Provider SHOULD allow the User to access to a Frequently Asked Questions (FAQ) section within their Wallet Instance to clarify doubts and resolve certain issues independently. Each actor SHOULD create specific FAQs and corresponding answers regarding the data and functionalities they provide to the Wallet Provider or in their Touchpoints. For certain error cases, the Wallet Provider SHOULD provide another actor's direct channel of support to facilitate timely management and avoid opening an assistance request within the Wallet Instance.

	2. **Level II | Requesting assistance** from the Wallet Provider: if Level I is insufficient, the Wallet Provider SHOULD give the User the possibility to open one or more assistance requests, perform a diagnosis and proceed with resolving the issue, if within their competence. These requests SHOULD be managed through the Wallet Instance or other Wallet Provider Touchpoints. The Wallet Provider MUST diagnose and resolve the issue if it falls under their responsibility.

	3. **Level III | Forwarding the request to the responsible actor**: if Level II is insufficient, the Wallet Provider SHOULD ensure that the request is forwarded to the responsible actor (Electronic Attestations of Attributes Provider, PID Provider, or Authentic Source), who ensures the availability of dedicated back-office channels to resolve the issue and communicate the outcome to the User.

Below are the User Experience requirements that the Wallet Solution Provider MUST guarantee through their own Wallet Solution:

- The User accesses to assistance options at any point during the User Experience, with a clear indication of how to access them;
- The User opens an assistance request through their Wallet Instance or other Touchpoints provided by the Wallet Provider;
- When a support request is open, the User receives prompt confirmation that the request has been acknowledged;
- The User is informed in advance if it is necessary to present their data with third parties;
- The User is informed when an assistance request needs to be managed outside of their Wallet Instance, such as on third-party channels;
- The User tracks the status of the request at any time through functionalities that MUST be made available by the actors dealing with the request.

User Feedback
--------------

User feedback collection allows for monitoring the User Experience, identifying potential areas for optimization, and continuously measuring the effectiveness of the service. Each Wallet Provider SHOULD establish a structured feedback collection system to monitor and improve the User Experience.

This feedback system MAY be fed by two different types of feedback collection:

- **Transactional Feedback** (Customer Effort Score, Customer Satisfaction): collected in response to specific actions, such as adding an Electronic Attestation or completing a presentation and verification process;
- **Relational Feedback** (Net Promoter Score): not in connection with specific actions, collected to measure the overall perception of the User in terms of satisfaction, loyalty, and likelihood of recommending the service to third-party users.

Here are some suggestions for implementing these types of feedback tools:

**Transactional Feedback Collection**

- **Customer Effort Score (CES)**: To measure the ease of use of the functionalities, surveys MAY be provided, for example, through components like modals or pop-ups within the Wallet Instance, triggered at the conclusion of specific actions or processes. Examples include:

	- After completing the process of obtaining an Electronic Attestation;
	- After the Authentication process, if positive;
	- After the presentation process, particularly at the end of the first presentation opportunity and no more than once every 6 months;
	- After the revocation and deactivation processes, to explore the reasons behind these actions.

- **Customer Satisfaction Survey (CSAT)**: To measure the overall satisfaction of the User after a prolonged period of using the Wallet Instance, surveys MAY be provided, for example, through modals or pop-ups within the Wallet Instance. It is recommended to use the CSAT at intervals of no less than six months and as an alternative to CES, to avoid overwhelming Users with too frequent surveys.

**Relational Feedback Collection**

- **Net Promoter Score (NPS)**: To measure User loyalty and the likelihood of recommending the service to others, an evaluation MAY be requested from the User once or twice a year, either through the same service delivery channel (e.g. the Wallet Instance) or external channels such as email or SMS. This should be aligned with the overall feedback collection strategy.


