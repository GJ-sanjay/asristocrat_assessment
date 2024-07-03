import subprocess

def run_behave_tests():
    # Execute Behave tests
    feature_directory = (
        "C://Users//sjayakumar//Downloads//aristocrat//features//login.feature"
    )
    subprocess.run(f"behave {feature_directory}", shell=True)


def generate_html_report():
    # Generate HTML report using pytest
    subprocess.run(
        "pytest C://Users//sjayakumar//Downloads//aristocrat//features//login.feature --html=report.html",
        shell=True,
    )


if __name__ == "__main__":
    # Run Behave tests
    run_behave_tests()

    # Generate HTML report after Behave tests execution
    generate_html_report()
