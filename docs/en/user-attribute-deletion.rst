.. include:: ../common/common_definitions.rst
.. Included via wallet-instance-functionalities.rst at title level '=' (document title).


User's Attributes Deletion
==========================

This Wallet Instance functionality allows Users to obtain a list of all Relying Parties towards which Digital Credentials have been presented. Subsequently Users may request deletion of the attributes of one or more Digital Credentials presented to a Relying Party of their choice. The Relying Party MUST uniquely identify those Digital Credentials by applying identity matching. Below the high level flow regarding this interaction is presented (:ref:`WP_115 <user-attribute-deletion-testcases>`).

.. plantuml:: plantuml/user-deletion-attribute-flow.puml
    :width: 99%
    :alt: The figure illustrates the Deletion of User's Attributes Process.
    :caption: `Deletion of User's Attributes Process. <https://www.plantuml.com/plantuml/svg/TLFDZjD03BxdAQnUkB3x03sWNR55ue8G2-B2nKcSTaGw3cDFIzyUUqeIfkpUHlNdxyTVyo2AIVDnX2SQIGD7u06-2QKt0e-gARHPIHhCoZ4VMqeDTie9DexP00faUpHDox_djISwXOwQoOX35oQC2fllE1ezV8oc5pigYpXDKAES01xt5FNAZ0t57epwol-5nak8U_XiEvTwSvTGSYBOnPx3ttMYIMlK1-efeQTquBGW1qEkKb0YmTqxTxWrpoV-IO3pCQ2VBpNasFa3ns1-mE6-vTjRU3xm6SOW2ZnKpWC9_8WXmiGY9FBApMzjF9jgfw07gky0oaQNw5SckOxxjSdLjQp-FEss9Z7XtNlxgP0qK21mDqkNaKmSXVmwaPM0JvHysW00V3NLcuQ1MyKGNHQAgxcX-V0m93xwf22EfDYZedd-Fw8Xl1pNRTOORkr5vP7tVk5_HTTaSqUuzGEZlydlyGAqYkfTl2tG9N5T0sOJZ1ewL9AImHkzByXXv3DqRDDet70su8A00mgqH14aTns937aSQxh-lhv0iR4wBrykhLLx-9QpuPKNcMMhX5_YLiLcN3g__JT_OWt3vShqO5RoSVm3>`_


.. .. figure:: ../../images/user's_data_deletion_flow.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/png/RLBDZjD03BxdAQozS67t0Nf0ksABn0KX5iI5YvCuxOZfE8mzBNrxx2bDcBAtTFpv-_7NHr7CMWwnmwASog6dtE6WdE7kcr2-0nGeOezTpx_1dzu8FDCn3DJDjXg6C6DIkFkECPB2nsICQQ2wYFCCBSe9u6b7II_Cs54QmQWl_5yedaFQmMVRERURsunICi4sZHp-hXFDsg8-q4WPDN1ouBmW9qSkKb0ZmVqxTxWnpqV-IO2gEVH52KQAL3ccaWR_m1ZC3pZSjtnx0ozxFa4Cei1JupoGm8yK4imiGYBEnDFrU4zNcLiRBwOwAEYUsZk0ij5b-bL8wdZrnzFgMbP_ddRJafZmzhqzLH93EWJkhz9r93Cd8RzEOYNW8sMVsc-0hwPwqp1mhnYIrBcxMXkw71wcp0UVLCI154TKDC__HpI4b-EwtHh3hRsg77dd5_vNT4csT8GRFp3wD_azNe4sKRsBjnMw96vhm6A2ISE0Ib8pUACF5Jb5Fi70Dat63IS3BWZOeq1FzY9b64XaAZ6sTED3Uu5gOtN-x7tJMhM7xxaONdcHMRPg-2LkKsp1fVFRV_CdrZ2TBqoFPgKSuXy0

..     Sequence Diagram for Deletion of User's Attributes

**Step 1:** The User requests the deletion of attributes invoking the Wallet Instance's attribute deletion function.

**Step 2:** The Wallet Instance collects all transaction data and shows the User the list of Relying Parties with which it has had interactions throughout the Wallet Instance lifecycle and are in possession of User's attributes (:ref:`WP_115a <user-attribute-deletion-testcases>`).

**Step 3:** The User selects the target Relying Party for attributes deletion.

**Steps 4 - 5:** The Wallet Instance obtains the Relying Party Entity Configuration at the Federation ./well-known/ endpoint. The URL or the Erasure Endpoint (``erasure_endpoint``) can be found inside the metadata parameter (:ref:`WP_116 <user-attribute-deletion-testcases>`).

**Step 6:** The Wallet Instance logs the Erasure Request's relevant information as defined in :ref:`wallet-instance-dashboard:Wallet Instance Dashboard and Transaction Logging`. These logs MUST include at least (:ref:`WP_117a <user-attribute-deletion-testcases>`):
  * the date of request,
  * the Relying Party to which the request was made,
  * the attributes requested to be removed.

**Steps 7 - 8:** The Wallet Instance redirects the User to the Erasure Endpoint. It MUST also ensure that a callback mechanism to allow the User-Agent to notify the Wallet Instance (and thus the User) after the Erasure Response is present (:ref:`WP_118 <user-attribute-deletion-testcases>`). Details on the Erasure Request can be found in :ref:`relying-party-provider-backend-endpoint:Relying Party Provider Backend Erasure Endpoint` (:ref:`WP_117 <user-attribute-deletion-testcases>`).

.. note::
  The Relying Party web page will authenticate the User with an appropriate Level of Assurance using any method such as CIE or the PID/IT-Wallet ID presentation. The specific mechanism used for authentication is left to the Relying Party. Upon authenticating the User, the Relying Party MAY prompt the User to perform additional steps needed for the deletion of attributes, e.g., it might require the User to confirm the deletion operation.

**Step 9:** Upon successful authentication of the User, the Relying Party MUST uniquely identify one or more Digital Credentials for which the User requests deletion by applying identity matching, and MUST delete the related attributes in its possession.

**Step 10:** The Relying Party returns the Erasure Response in the form of an HTTP Response to the User-Agent and includes the callback URL if provided in the Erasure Request. Details on the Erasure Response can be found in :ref:`relying-party-provider-backend-endpoint:Relying Party Provider Backend Erasure Endpoint`.

**Steps 11 - 12:** The User-Agent uses the implemented method to return the Erasure Response to the Wallet Instance. Finally, the User is notified via the Wallet Instance regarding the Erasure Response outcome (:ref:`WP_119 <user-attribute-deletion-testcases>`).


