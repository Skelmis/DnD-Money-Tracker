from piccolo.table import Table
from piccolo.columns import Real, Text, Boolean


class Money(Table):
    entity: str = Text(help_text="The entity this money concerns")
    copper: float = Real()
    silver: float = Real()
    electrum: float = Real()
    gold: float = Real()
    platinum: float = Real()
    use_platinum: bool = Boolean(
        default=False, help_text="Whether to use platinum or not"
    )
    use_electrum: bool = Boolean(
        default=False, help_text="Whether to use electrum or not"
    )

    async def order_money(self):
        """Recalculates money to the highest common denominator"""
        total_copper: float = (
            self.copper
            + (self.silver * 10)
            + (self.electrum * 50)
            + (self.gold * 100)
            + (self.platinum * 1000)
        )
        if self.use_platinum:
            platinum, leftover = divmod(total_copper, 1000)
            self.platinum = platinum
        else:
            leftover = total_copper
            self.platinum = 0

        gold, leftover = divmod(leftover, 100)
        if self.use_electrum:
            electrum, leftover = divmod(leftover, 50)
            self.electrum = electrum
        else:
            self.electrum = 0

        silver, copper = divmod(leftover, 10)

        self.gold = gold
        self.silver = silver
        self.copper = copper
        await self.save()
