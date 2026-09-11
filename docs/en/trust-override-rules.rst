.. include:: ../common/common_definitions.rst
.. Included via trust-evaluation.rst at title level '-' (level 1).

Authorization Decision and Override Rules
------------------------------------------

The Authorization Decision can either be ``AUTHORIZED`` or ``NOT_AUTHORIZED``.
The conditions that determine this outcome depend on the specific Authorization Validation procedure followed.

- In case the Wallet Unit follows the :ref:`trust-evaluation:EUDIW Authorization` evaluation path, then the outcome is:

    - ``AUTHORIZED`` if the process terminates with ``REGISTER_VALID`` OR ``CERTIFICATE_VALID`` AND ``EDP_SATISFIED`` AND ``VERIFICATION_PASSED``; or
    - ``NOT_AUTHORIZED`` otherwise.

- In case the Wallet Unit follows the National :ref:`trust-evaluation:Authorization` evaluation path, then the outcome is:

    - ``AUTHORIZED`` if the process terminates with ``TRUST_MARK_VALID`` AND ``ENTITLEMENT_VALID`` AND ``VERIFICATION_PASSED``; or,
    - ``NOT_AUTHORIZED`` otherwise.

**Override Principles**

A ``NOT_AUTHORIZED`` decision can be either *non-overridable* (the Wallet Unit blocks the interaction) or *overridable* (the Wallet Unit presents the negative outcome and the User can choose to proceed).

- During **Credential Issuance** phase, all negative verification outcomes MUST be *non-overridable*: the Wallet Unit MUST NOT let the User interact with providers whose registration cannot be confirmed.

- During the **Presentation** phase, all negative verification outcomes MUST be *non-overridable*, except for the following cases:

    - **Overasking [EUDIW]**.
      When the process terminates with ``REGISTER_VALID`` OR ``CERTIFICATE_VALID`` AND ``OVERASKING_DETECTED``, i.e., the Authorization Artifact Validation has had a positive outcome, but the Scope Comparison finds the Relying Party requesting more than its registered scope.
    - **Negative Embedded Disclosure Policy evaluation [EUDIW]**.
      When the process terminates with ``REGISTER_VALID`` OR ``CERTIFICATE_VALID`` AND ``EDP_NOT_SATISFIED``, i.e., the Authorization Artifact Validation has had a positive outcome but the Embedded Disclosure Policy would not allow the presentation to the Relying Party.
    - **Overasking [National]**.
      When the process terminates with ``TRUST_MARK_VALID`` AND ``OVERASKING_DETECTED``, i.e., the :ref:`trust-evaluation:Trust Mark Validation` has had a positive outcome, but the :ref:`trust-evaluation:Overasking Check` finds the Relying Party requesting more than its registered scope.

All other presentation failures, including binding failures or intermediary binding failures, MUST NOT be overridable as they indicate an integrity problem rather than a user-facing choice.

In case of non-overridable failures, the Wallet Unit MUST clearly inform the User about the negative outcome.
User-relevant information about overridable outcomes MUST be presented as advisories, and the User approval MUST be a separate step from the final Authorization Decision.

.. note::
    **User opt-in**.
    The *Scope Comparison Procedure* in :ref:`trust-evaluation:Authorization Validation` is executed only if the User enabled registration verification.
    Override mechanisms define what happens when the procedure produces a negative result.
