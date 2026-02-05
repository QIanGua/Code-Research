# OpenCodeInterpreter Research Report

## 1. Introduction

**OpenCodeInterpreter** is a suite of open-source code generation systems designed to bridge the gap between open-source Large Language Models (LLMs) and sophisticated proprietary systems like the GPT-4 Code Interpreter.

The primary goal of this project is to significantly enhance code generation capabilities by integrating **execution** and **iterative refinement** functionalities directly into the generation process. This allows the model to not only generate code but also "run" it (in a simulated or actual environment), observe the output, and correct errors, mimicking the workflow of a human developer.

## 2. Key Features

*   **Integration of Execution Feedback**: Unlike traditional code generation models that output a static code block, OpenCodeInterpreter can utilize feedback from code execution to refine its output.
*   **Iterative Refinement**: The system supports multi-turn interactions where the model can improve its code based on error messages or incorrect outputs from previous execution attempts.
*   **Open Source**: The project provides open access to its models, datasets, and evaluation code, fostering transparency and further research.
*   **Wide Range of Models**: It offers models of various sizes (from 1.3B to 70B parameters) and base architectures (DeepSeek-Coder, CodeLlama, StarCoder2).

## 3. Models and Performance

The OpenCodeInterpreter series includes models based on different foundational architectures:

*   **OpenCodeInterpreter-DS**: Based on DeepSeek-Coder (1.3B, 6.7B, 33B)
*   **OpenCodeInterpreter-CL**: Based on CodeLlama (7B, 13B, 34B, 70B)
*   **OpenCodeInterpreter-SC2**: Based on StarCoder2 (3B, 7B, 15B)
*   **OpenCodeInterpreter-GM**: Based on Gemma (7B)

### Performance Impact of Execution Feedback

The integration of execution feedback leads to significant performance improvements on standard benchmarks like **HumanEval** and **MBPP**. The table below highlights the "Average (+)" score improvement for selected models:

| Model Variant | Base Score (Avg+) | With Execution Feedback (Avg+) | Improvement |
| :--- | :--- | :--- | :--- |
| **DS-6.7B** | 67.9 | 75.6 | **+7.7** |
| **DS-33B** | 70.4 | 76.4 | **+6.0** |
| **CL-70B** | 66.3 | 73.7 | **+7.4** |
| **SC2-15B** | 65.4 | 67.7 | **+2.3** |

*Note: The "(+)" notation refers to extended versions of the benchmarks (HumanEval+ and MBPP+).*

## 4. Methodology

### Data Collection
The project utilizes the **Code-Feedback** dataset, which features approximately 68,000 multi-turn interactions. This dataset is crucial for training the models to handle execution feedback and dynamic code refinement. The data collection process involves a command-line interface adapted from `Local-Code-Interpreter`.

### Evaluation
The evaluation framework is built upon **EvalPlus**. It supports:
*   **Single-turn Evaluation**: Standard code generation assessment.
*   **Multi-turn Evaluation**: Specifically designed to test the model's ability to use execution feedback to fix bugs and improve code quality over multiple rounds.

## 5. Usage & Quick Start

The project provides a local demo that allows users to generate and execute code with automated feedback.

### Quick Start Steps
1.  Clone the repository:
    ```bash
    git clone https://github.com/OpenCodeInterpreter/OpenCodeInterpreter.git
    cd demo
    ```
2.  Set up the environment:
    ```bash
    conda create -n demo python=3.10
    conda activate demo
    pip install -r requirements.txt
    ```
3.  Run the Gradio App:
    ```bash
    python3 chatbot.py --path "m-a-p/OpenCodeInterpreter-DS-6.7B"
    ```

## 6. Resources

*   **GitHub Repository**: [OpenCodeInterpreter/OpenCodeInterpreter](https://github.com/OpenCodeInterpreter/OpenCodeInterpreter)
*   **Paper**: [arXiv:2402.14658](https://arxiv.org/abs/2402.14658)
*   **Hugging Face Collection**: [OpenCodeInterpreter Models](https://huggingface.co/collections/m-a-p/opencodeinterpreter-65d312f6f88da990a64da456)
*   **Dataset**: [Code-Feedback](https://huggingface.co/datasets/m-a-p/Code-Feedback)

---
*Report generated based on repository analysis as of Oct 2025.*
