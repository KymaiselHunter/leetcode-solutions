import os

def update_readme(readme_path, solutions_dir):
    # Read the current README
    if os.path.exists(readme_path):
        with open(readme_path, 'r') as file:
            lines = file.readlines()
    else:
        lines = []

    # Find the marker where we want to insert or update the list of solutions
    marker = "<!-- SOLUTIONS -->"
    if marker not in lines:
        lines.append(f"\n{marker}\n")

    # Get the index of the marker line
    marker_index = lines.index(f"{marker}\n") + 1

    # Scan the solutions directory (e.g., 'leetcode') and build a list of solution links
    solution_links = []
    for root, dirs, files in os.walk(solutions_dir):
        for file in sorted(files):
            if file.endswith('.py') or file.endswith('.cpp'):
                relative_path = os.path.relpath(os.path.join(root, file), solutions_dir)
                solution_links.append(f"- [{file}](leetcode/{relative_path})\n")

    # Replace the section in the README after the marker
    lines = lines[:marker_index] + solution_links

    # Write the updated README back
    with open(readme_path, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    readme_path = "README.md"
    solutions_dir = "leetcode"
    update_readme(readme_path, solutions_dir)
