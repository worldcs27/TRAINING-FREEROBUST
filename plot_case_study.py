import matplotlib.pyplot as plt

def create_case_study_image():
    # 创建一个画布
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')
    
    # 标题
    plt.text(0.5, 0.95, "Figure 2: Qualitative Comparison on Deep Trap Data", 
             ha='center', va='center', fontsize=14, fontweight='bold')

    # === 左边：Baseline (Failure) ===
    plt.text(0.05, 0.85, "Baseline (Standard Prompting)", fontsize=12, fontweight='bold', color='red')
    
    code_baseline = (
        "User Query: 'Calculate mean of amount'\n"
        "-------------------------------------\n"
        ">>> Generated Code:\n"
        "df['amount'].mean()\n\n"
        ">>> Execution Output:\n"
        "TypeError: Could not convert string\n"
        "'6274...$9,999' to numeric\n"
        "\n"
        "[SYSTEM CRASH] ❌"
    )
    
    # 画一个红色的框表示失败
    bbox_props_fail = dict(boxstyle="round,pad=0.5", fc="#ffe6e6", ec="red", lw=2)
    plt.text(0.05, 0.45, code_baseline, fontsize=10, fontfamily='monospace', 
             bbox=bbox_props_fail, va='center')

    # === 中间：箭头 ===
    plt.arrow(0.48, 0.5, 0.04, 0, head_width=0.02, head_length=0.02, fc='black', ec='black')

    # === 右边：Ours (Success) ===
    plt.text(0.55, 0.85, "Ours (Schema-Aware Reflection)", fontsize=12, fontweight='bold', color='green')
    
    code_ours = (
        "[Step 1] Error Detected: TypeError\n"
        "[Step 2] Inject Schema: columns=['amount']\n"
        "[Step 3] Refined Code Generation:\n"
        "-------------------------------------\n"
        ">>> Generated Code:\n"
        "df['amount'].str.replace(r'[$,]', '', regex=True)\n"
        "            .astype(float).mean()\n\n"
        ">>> Execution Output:\n"
        "3333.1666...\n"
        "\n"
        "[SUCCESS] ✅"
    )
    
    # 画一个绿色的框表示成功
    bbox_props_success = dict(boxstyle="round,pad=0.5", fc="#e6ffe6", ec="green", lw=2)
    plt.text(0.55, 0.45, code_ours, fontsize=10, fontfamily='monospace', 
             bbox=bbox_props_success, va='center')

    # 保存图片
    plt.tight_layout()
    plt.savefig("case_study.png", dpi=300)
    print("✅ 图片已生成: case_study.png")
    print("请把这张图片上传到 Overleaf！")

if __name__ == "__main__":
    create_case_study_image()