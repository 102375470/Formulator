from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTabWidget

from qt.components import ComboWithLabel, SpinWithLabel, TextWithLabel, LabelWithLabel, TableWithLabel
from base.constant import SHIELD_BASE_MAP


class DashboardWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        top = QWidget()
        top_layout = QHBoxLayout(top)
        layout.addWidget(top)

        self.fight_select = ComboWithLabel("选择战斗")
        top_layout.addWidget(self.fight_select)
        self.target_level = ComboWithLabel("目标等级", items=[str(level) for level in SHIELD_BASE_MAP])
        top_layout.addWidget(self.target_level)
        self.duration = SpinWithLabel("战斗时长", maximum=3600, value=180)
        top_layout.addWidget(self.duration)

        self.button = QPushButton(text="开始模拟!")
        layout.addWidget(self.button)

        bottom = QWidget()
        bottom_layout = QHBoxLayout(bottom)
        layout.addWidget(bottom)

        tab = QTabWidget()
        bottom_layout.addWidget(tab, 2)
        result = QWidget()
        result_layout = QVBoxLayout(result)
        bottom_layout.addWidget(result, 1)

        attribute = QWidget()
        attribute_layout = QHBoxLayout(attribute)
        tab.addTab(attribute, "属性")

        self.init_attribute = TableWithLabel("增益前属性", column_count=2)
        attribute_layout.addWidget(self.init_attribute)
        self.final_attribute = TableWithLabel("增益后属性", column_count=2)
        attribute_layout.addWidget(self.final_attribute)

        detail = QWidget()
        detail_layout = QVBoxLayout(detail)
        tab.addTab(detail, "伤害总结")
        self.details = {}
        self.skill_combo = ComboWithLabel("选择技能")
        detail_layout.addWidget(self.skill_combo)
        self.status_combo = ComboWithLabel("选择增益")
        detail_layout.addWidget(self.status_combo)
        detail_table = QWidget()
        detail_table_layout = QHBoxLayout(detail_table)
        self.damage_detail = TableWithLabel("伤害细节", column_count=2)
        detail_table_layout.addWidget(self.damage_detail)
        self.gradient_detail = TableWithLabel("属性收益", column_count=2)
        detail_table_layout.addWidget(self.damage_detail)
        detail_layout.addWidget(detail_table)

        detail_layout.addStretch()

        self.summary = TableWithLabel("伤害统计", headers=["技能/次数", "命中/%", "会心/%", "伤害/%"])

        tab.addTab(self.summary, "战斗总结")

        self.dps = LabelWithLabel("每秒伤害")
        result_layout.addWidget(self.dps)

        self.gradients = TableWithLabel("属性收益", column_count=2)

        result_layout.addWidget(self.gradients)

        result_layout.addStretch()

        layout.addStretch()



