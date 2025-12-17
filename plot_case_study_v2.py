import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_case_study_image_v2():
    print("正在生成 Case Study 对比图 (V2稳健版)...")
    
    # 1. 创建画布，稍微大一点
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # 2. 关键修复：强制设定坐标轴范围为 0-1，并隐藏坐标轴
    # 这样可以确保我们放置的元素绝对不会跑出画面
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    # ================= 内容定义 =================
    # 标题
    plt.text(0.5, 0.97, "Figure 2: Qualitative Comparison on 'Deep Trap' Data (Hidden $9,999 at Row 100)", 
             ha='center', va='top', fontsize=16, fontweight='bold')

    # 左侧文本 (Baseline)
    code_baseline_title = "Baseline (Standard Prompting)"
    code_baseline_content = (
        "User Query: 'Calculate mean of amount'\n"
        "-------------------------------------\n"
        "👀 Model sees clean head(), generates:\n"
        ">>> df['amount'].mean()\n\n"
        "💥 Execution hits row 100 ('$9,999'):\n"
        ">>> TypeError: Could not convert string\n"
        "    '6274...$9,999' to numeric\n"
        "\n"
        "-------------------------------------\n"
        "RESULT: [SYSTEM CRASH] ❌"
    )
    
    # 右侧文本 (Ours)
    code_ours_title = "Ours (Schema-Aware Reflection)"
    code_ours_content = (
        "[Step 1] 🚨 Error Detected: TypeError caught.\n"
        "[Step 2] 🧠 Reflection triggered.\n"
        "         Inject Schema: columns=['amount']\n"
        "[Step 3] ✨ Refined Code Generation:\n"
        "-------------------------------------\n"
        ">>> df['amount'].str.replace(r'[$,]', '', regex=True)\n"
        "            .astype(float).mean()\n\n"
        "✅ Execution Successful:\n"
        ">>> 3333.1666...\n"
        "\n"
        "-------------------------------------\n"
        "RESULT: [SUCCESS & CORRECT] ✅"
    )

    # ================= 绘图区域 =================
    
    # 1. 画左边的红框 (Baseline)
    # 使用左上角对齐 (ha='left', va='top') 更容易控制位置
    bbox_props_fail = dict(boxstyle="round,pad=0.8", fc="#fff0f0", ec="red", lw=3)
    ax.text(0.05, 0.85, code_baseline_title, fontsize=14, fontweight='bold', color='darkred', ha='left')
    ax.text(0.05, 0.80, code_baseline_content, fontsize=11, fontfamily='monospace', 
             bbox=bbox_props_fail, ha='left', va='top')

    # 2. 画中间的箭头
    # 使用 FancyArrowPatch 画一个更明显的胖箭头
    arrow = patches.FancyArrowPatch((0.48, 0.5), (0.54, 0.5), 
                                    connectionstyle="arc3,rad=0", 
                                    color="black", 
                                    arrowstyle="Simple, tail_width=2, head_width=10, head_length=10",
                                    lw=2)
    ax.add_patch(arrow)

    # 3. 画右边的绿框 (Ours)
    bbox_props_success = dict(boxstyle="round,pad=0.8", fc="#f0fff0", ec="green", lw=3)
    ax.text(0.56, 0.85, code_ours_title, fontsize=14, fontweight='bold', color='darkgreen', ha='left')
    ax.text(0.56, 0.80, code_ours_content, fontsize=11, fontfamily='monospace', 
             bbox=bbox_props_success, ha='left', va='top')

    # 保存图片 (不使用 tight_layout，避免裁剪过度)
    plt.savefig("case_study_v2.png", dpi=300, bbox_inches='tight')
    print("✅ 图片已成功生成: case_study_v2.png")
    print("请检查图片内容，然后上传到 Overleaf。")

if __name__ == "__main__":
    create_case_study_image_v2()