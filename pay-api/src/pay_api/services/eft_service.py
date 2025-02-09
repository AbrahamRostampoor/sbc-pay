# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Service to manage CFS EFT Payments."""

from pay_api.utils.enums import PaymentMethod

from .deposit_service import DepositService
from .invoice import Invoice
from .invoice_reference import InvoiceReference
from .payment_account import PaymentAccount
from .payment_line_item import PaymentLineItem


class EftService(DepositService):
    """Service to manage electronic fund transfers."""

    def get_payment_method_code(self):
        """Return EFT as the system code."""
        return PaymentMethod.EFT.value

    def create_invoice(self, payment_account: PaymentAccount, line_items: [PaymentLineItem], invoice: Invoice,
                       **kwargs) -> InvoiceReference:
        """Return a static invoice number for direct pay."""
        # Do nothing here as the invoice references will be created later for eft payment reconciliations (TDI17).

    def apply_credit(self, invoice: Invoice) -> None:
        """Apply credit to the invoice."""
        self._release_payment(invoice=invoice)
