import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_case_study_image_v3():
    print("正在生成 Case Study 对比图 (V3 终极防裁剪版)...")
    
    # 1. 加宽画布 (从12增加到14)，确保右边有足够空间
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # 设定坐标轴范围，确保元素在画面内
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    # ================= 内容定义 =================
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
    
    # 右侧文本 (Ours) - 关键修改：长代码手动换行
    code_ours_title = "Ours (Schema-Aware Reflection)"
    code_ours_content = (
        "[Step 1] 🚨 Error Detected: TypeError caught.\n"
        "[Step 2] 🧠 Reflection triggered.\n"
        "         Inject Schema: columns=['amount']\n"
        "[Step 3] ✨ Refined Code Generation:\n"
        "-------------------------------------\n"
        ">>> df['amount'].str.replace(           \n"  # 手动换行
        "        r'[$,]', '', regex=True)       \n"  # 缩进对齐
        "        .astype(float).mean()\n\n"
        "✅ Execution Successful:\n"
        ">>> 3333.1666...\n"
        "\n"
        "-------------------------------------\n"
        "RESULT: [SUCCESS & CORRECT] ✅"
    )

    # ================= 绘图区域 =================
    
    # 左边红框
    bbox_props_fail = dict(boxstyle="round,pad=0.8", fc="#fff0f0", ec="red", lw=3)
    ax.text(0.02, 0.85, code_baseline_title, fontsize=14, fontweight='bold', color='darkred', ha='left')
    ax.text(0.02, 0.80, code_baseline_content, fontsize=11, fontfamily='monospace', 
             bbox=bbox_props_fail, ha='left', va='top')

    # 中间箭头 (稍微左移)
    arrow = patches.FancyArrowPatch((0.45, 0.5), (0.51, 0.5), 
                                    connectionstyle="arc3,rad=0", 
                                    color="black", 
                                    arrowstyle="Simple, tail_width=2, head_width=10, head_length=10",
                                    lw=2)
    ax.add_patch(arrow)

    # 右边绿框 (位置左移至 0.53，防止右边溢出)
    bbox_props_success = dict(boxstyle="round,pad=0.8", fc="#f0fff0", ec="green", lw=3)
    ax.text(0.53, 0.85, code_ours_title, fontsize=14, fontweight='bold', color='darkgreen', ha='left')
    ax.text(0.53, 0.80, code_ours_content, fontsize=11, fontfamily='monospace', 
             bbox=bbox_props_success, ha='left', va='top')

    # 保存图片
    plt.savefig("case_study_v3.png", dpi=300, bbox_inches='tight')
    print("✅ 图片已成功生成: case_study_v3.png")

if __name__ == "__main__":
    create_case_study_image_v3()