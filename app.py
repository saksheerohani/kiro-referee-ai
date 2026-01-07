def compare_options(problem, option_a, option_b, constraints):
    result = {
        "problem": problem,
        "constraints": constraints,
        "options": {
            option_a: {
                "pros": ["Low cost", "Easy to deploy"],
                "cons": ["Limited scalability"]
            },
            option_b: {
                "pros": ["High scalability", "Future-ready"],
                "cons": ["Higher cost", "Complex setup"]
            }
        }
    }

    return result


if __name__ == "__main__":
    decision = compare_options(
        problem="Backend choice for a Bharat-scale app",
        option_a="Serverless (AWS Lambda)",
        option_b="VM-based Backend (EC2)",
        constraints=["Low budget", "Millions of users"]
    )

    for k, v in decision.items():
        print(k, ":", v)
