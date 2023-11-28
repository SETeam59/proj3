# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change. 

Please note we have a code of conduct (CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.

## Pull Request Process

1. Maintain GITS project quality.
2. Should have appropriate ISSUE linked with the Pull request.
3. The PR should be assigned to the indiividual requesting a merge.
4. The Reviewers must approve the pull request before merge the code.
5. The description should be updated as to what has been asked in the issue.
6. All the development code should accompany unit test cases to suppor the validation results.
7. Travis Builds should be passing while the code is generated.
8. The development code should be style checked, well formatted and syntax error free. Use of pep8, autoflake8 and flake8 tools will enable the users to get the required code quality.
9. Commit messages should company details of the changes been made.

## Bug Report Process

Bugs are tracked as GitHub issues. You need to create an issue and include all the following details if possible.

Explain the problem and include additional details to help maintainers reproduce the problem:

1. Before raising a GitHub issue, make sure that you are running the latest version of the application and have all recommended OS updates / patches installed
2. Use a clear and descriptive title for the issue to identify the problem.
3. Describe the exact steps which reproduce the problem in as many details as possible. For example, start by explaining how you started Atom, e.g. which command exactly you used in the terminal, or how you started Atom otherwise. When listing steps, don't just say what you did, but explain how you did it. For example, if you moved the cursor to the end of a line, explain if you used the mouse, or a keyboard shortcut or an Atom command, and if so which one?
4. Provide specific examples to demonstrate the steps. Include links to files or GitHub projects, or copy/pasteable snippets, which you use in those examples. If you're providing snippets in the issue, use Markdown code blocks.
5. Describe the behavior you observed after following the steps and point out what exactly is the problem with that behavior.
6. Explain which behavior you expected to see instead and why.
7. Include screenshots and animated GIFs which show you following the described steps and clearly demonstrate the problem.


## Enhancement suggestion process / Feature request Process

Bugs are tracked as GitHub issues. You need to create an issue and include all the following details if possible.
1. Use a clear and descriptive title for the issue to identify the suggestion.
2. Provide a step-by-step description of the suggested enhancement in as many details as possible.
3. Provide specific examples to demonstrate the steps.
4. Describe the current behavior and explain which behavior you expected to see instead and why.
5. Explain why this enhancement would be useful to most users and isn't something that can or should be implemented as a community package.
6. List some other repo or applications where this enhancement / feature exists. ( this is optional )

### Problem Explanation
Clearly articulate the issue and include additional details that can aid maintainers in reproducing the problem.

### Verify Your Environment:
Ensure that you are running the latest version of the application and have all recommended OS updates and patches installed before raising a GitHub issue.

### Use a Descriptive Title:
Employ a clear and descriptive title for the issue, facilitating the identification of the problem.

### Detailed Steps:
Explicitly describe the exact steps needed to replicate the problem. Include a comprehensive account of the process, from the initial command or action to the observed issue.

### Specific Examples:
Back your description with specific examples, links to files or GitHub projects, or code snippets that support the problem's reproduction.

### Observed Behavior:
Explain the behavior you encountered following the specified steps and outline the issue's nature.

### Expected Behavior:
Clearly state what behavior you anticipated and why it differs from what you observed.

### Visual Aids:
If possible, include screenshots or animated GIFs that visually depict the issue as you followed the described steps.

### Enhancement Suggestion Process / Feature Request Process:
For enhancement suggestions or feature requests, kindly adhere to the following guidelines when creating an issue:

### Descriptive Title:
Utilize a clear and descriptive title for the issue, making the suggestion easily identifiable.

### Specific Examples:
Support your suggestion with specific examples that illustrate the proposed steps and outcomes.

### Current Behavior:
Describe the existing behavior and elucidate why the suggested enhancement is preferable.

### Utility to Users:
Explain how this enhancement would benefit the majority of users and clarify why it's not suited for implementation as a community package.

## Style Checker and Analyzer
We are using black as our style checkers and code analyzer. While contrivuting to this project, make sure you conform to norms dictated by black

### black
<b>Installation</b>
- `python<version> -m pip install black`

 <b>Using black</b> 
 <br/>To start using black, open an interactive shell and run the following. This will automatically refractor the code according the black guidelines
- `black path/to/code/to/check.py`
