class CardService:
    def __init__(self, card_number: str):
        self.card_number = card_number

    def process_payment(self, amount: int):
        print(
            f"SRP bad 결제 진행: {amount}원이 후불신용카드({self.card_number[-3:]})로 결제됨")


srp_card = CardService('xxx-xxx-xxx-SRP').process_payment(1000)
