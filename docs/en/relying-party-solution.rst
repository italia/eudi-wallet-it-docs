.. include:: ../common/common_definitions.rst
.. Included via entities.rst at title level '=' (document title).


Relying Party Solution
======================

A Relying Party, as an Organizational entity relying upon IT-Wallet, provides Technical Solutions (Relying Party Solution) that could combine software, hardware, services, settings, and configurations, including Relying Party Instances for User authentication and Digital Credential verification.

In order to implement and provide Technical Solutions, a Relying Party may rely on the services of a **Relying Party Intermediary**. Pursuant to Article 5b(8) of `EU_2024_1183`_, intermediaries acting on behalf of Relying Parties are deemed to be Relying Parties and **shall not store data about the content of the transaction** between the Wallet User and the intermediated Relying Party. For the complete definitions and the underlying European legal framework, see **Relying Party Intermediary** in :ref:`defined-terms:Defined Terms and Acronyms`.

.. note::
  In the implementation profile described by these technical specifications, a Relying Party Intermediary is also an OpenID Federation Intermediate Entity.

A Relying Party provides at least one of the following components:

- **Relying Party Backend**: It handles Relying Party Instances registration and the relative Certificate management. It obtains X.509 Certificate according to the :ref:`infrastructure-trust:Infrastructure of Trust`. It SHOULD also provide a X.509 Certificate to its Relying Party Instances. It also may implement additional web services and business logic for its own purposes and use cases.
- **Relying Party Instance**: It is a frontend provided to Users in order to access Relying Party Services, and it may be provided as:

  - **Web Client**.
  - **Mobile Application**.

The following diagram depicts the Relying Party Solution High Level Architecture.

.. plantuml:: plantuml/rp-solution-architecture.puml
    :width: 99%
    :alt: The figure illustrates the Relying Party Solution High Level Architecture.
    :caption: `Relying Party Solution High Level Architecture. <https://www.plantuml.com/plantuml/svg/jLHDRzim3BtxLt2vD0NMxTBZC3HD0zJOXXbjYc8dGvQPM9Wi2QBSBXZwtqV9YTtKBOOT5Y2HIVFZlKSn5nI43rshuGRrJfaj56pluDRgBYXhu5fj6_YA3wXXuMMZ0ihGUSpUAIDrLoDyMfv_N9wNIziwQz24prbsdL-jojlrwcRrVVsZMCrFi-m4hd2Z38AGmNe2OMgW7GLiAIlGapNpZj2_XzaT7pC-LnmHNV2eGWFv-knUQ8rXniKouC_Gi5pz2lFWEmgbCBAniSWwch18PYmMlpbHXyGyjug25udT4drG6oL5m1wJy_P1rMmKNtAGmebAQHKKEpRMGsWGkAFoE082bBPdag1bbxOpjV2xkUy5BLqKjApsRWRokjApK_XzJ6pkNLa9-HDDFScwxFq7RjUCNKTo1UI60kk0u9yJZTpaI1PQOSGMM-xo0VBMwVH8K7Ma31A1jbib4sToA6DM70P8GKZCC-9CFoDRLwfzvpUv3jW6hXE-ZrYLKYksEFaUArWcuy2JFMSLOwXXuwq9oAmK7tuZ92QqyVQ0w48JnoH7xbTgguBGiFHOnrVy-80-gT6B_pgSrlByiHJESVDloO25StgVbc0DR_udigViASjkqpLBz_qntRr1yYXDyemIxrVfX8OEVKJ2_7mZFUhKYHhbABjKFBBzBawRtANn7mMz75eUMGiPA2tk9FXOqabmnh4lbddSWhylCGGRY_HbniGfokAmv-o5HP5Jofoa7U5zEwtdE1dAfEjYF_xn_wOVDHjo6F-nS9EY4qp_LlI2UNMj_WC0>`_

.. .. figure:: ../../images/relying_party_solution_high_level_architecture.svg
..   :width: 100%
..   :alt: The image illustrates the Relying Party Solution and its relations and interactions within the ecosystem.
..   :target: https://www.plantuml.com/plantuml/svg/jLHDRziy3BxxL_3DfIdmfhdij5FJD42DhPZHfYXsCcIPIOJ9aY39pOAX_tsadDZDl6BOOGOIcHG_deSVlWvH-DWsEljF6QdR6c4NemiVvtClzbTR5NTjrGRqqfg89bv9syoT5ePzPY7MMbNpvOTPmQgd-y_pHeI8dbJbqZRE6lPn73-xoszNvUDwzR3wilvQhAQNMNO1jxXH1a78Q7q0OMe81mhGXAn07woPSkx_OV94nuJE5Lcm2lQ43FBrx5beZN52mJAWfqzQhhx7QVHjYAKmScSvo9f5MB2OWl4l3w7500-uLI5w4PKri4GVrKP94R73vBnzKJK9nQSSf72YKbf5HOgDzH1t29HHUHm00KhRCKdGiXlRcbhumzIZFYYpBPtmyL1MHpK1UUWkeE0BUBIwPIoJI_XnJcpgNLa9-GrDFVAwwVGdRdU4NJEv0d8JeZ0ImRybojpaG1OQOSGM6-uPv8tJwJK03O0o609ekrKoSGuE9NjnCq2AW85u0ZtfRs3hIdNC_2xN7blFTSHtZrKfjIA9d9-nWcKIZZnPCwi8GmqRdyQq1aM7tmY92IrF3uWsxhXDSk1-gxOg2WrBZpLVqUiB-bIDhlY_XzDOwZ-MmZbAVfy4M3YdJsuCgx_vbyXUizSiUqnZbkPzdsQlBpcN9cc64XzNwIBq6JgBXFdjHdhKALFOAHUo6qKjE-xYECbJQl-PqQzDovcra36anHqPdvLqR9onxVao3rlmvoM6Q3b85sPm7ACiJdjEMbWKUUWypzr6UDzpwpYEcZBAkkZQFtnlZgqcGVRjFolSAEW8qry6lIPURQD_0W00

..   Relying Party Solution High Level Architecture


.. toctree::
  :caption: Relying Party Solution Table of Contents
  :maxdepth: 3

  relying-party-instance.rst
  relying-party-entity-configuration.rst
  relying-party-metadata.rst


