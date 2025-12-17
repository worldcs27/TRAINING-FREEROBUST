import pandas as pd
import numpy as np

def generate_deep_traps():
    print(">>> 正在生成【深层陷阱】数据集 (Hidden Deep Traps)...")

    # === 陷阱 1: 货币符号藏在第 100 行 ===
    # 构造 99 行干净数据
    df_clean = pd.DataFrame({
        "id": range(99),
        "amount": np.random.randint(100, 1000, size=99) # 纯整数
    })
    # 构造 1 行脏数据
    df_dirty = pd.DataFrame({
        "id": [100],
        "amount": ["$9,999"] # 脏数据
    })
    # 合并
    df_currency = pd.concat([df_clean, df_dirty], ignore_index=True)
    df_currency.to_csv("trap_deep_currency.csv", index=False)
    print("✅ 生成 trap_deep_currency.csv (前99行干净，最后1行脏)")

    # === 陷阱 2: 混合单位藏在深处 ===
    df_clean_units = pd.DataFrame({
        "item": [f"Item_{i}" for i in range(99)],
        "weight": np.random.randint(10, 50, size=99) # 纯整数
    })
    df_dirty_units = pd.DataFrame({
        "item": ["Item_100"],
        "weight": ["100kg"] # 突然出现单位
    })
    df_units = pd.concat([df_clean_units, df_dirty_units], ignore_index=True)
    df_units.to_csv("trap_deep_units.csv", index=False)
    print("✅ 生成 trap_deep_units.csv")
    
    print("\n这就是大模型的'盲区'：它只看前几行，以为数据很干净，结果掉进坑里。")

if __name__ == "__main__":
    generate_deep_traps()