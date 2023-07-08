class SRPPaymentGateway:
    def srp_process_payment(self, card_num: str, amount: int):
        print(
            f"SRP good 결제 진행: {amount}원이 후불신용카드({card_num[-3:]})로 결제됨")


class CreditCard:
    def __init__(self, card_num: str):
        self.card_num = card_num


class CardService:
    def __init__(self, my_card: CreditCard, pay_gw: SRPPaymentGateway):
        self.my_card = my_card
        self.pay_gw = pay_gw
        if not isinstance(pay_gw, SRPPaymentGateway):
            raise Exception("OCPPaymentGateway가 아님")

    def pay_after(self, amount: int):
        card_num = self.my_card.card_num
        self.pay_gw.srp_process_payment(card_num, amount)


srp_card = CreditCard('xxx-xxx-xxx-SRP')
srp_pay_gw = SRPPaymentGateway()
card_service = CardService(srp_card, srp_pay_gw).pay_after(1000)
