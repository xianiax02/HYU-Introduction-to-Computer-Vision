

print("Cloning the GitHub repository...")
!git clone https://github.com/xianiax02/HYU-Introduction-to-Computer-Vision.git

print("Verifying the cloned repository contents...")
!ls HYU-Introduction-to-Computer-Vision

print("Please enter your Git username. For example, 'Your Name'")
!git config user.name "Your Name"

print("Changing directory to the cloned repository...")
%cd HYU-Introduction-to-Computer-Vision

print("Please enter your Git username. For example, 'Your Name'")
!git config user.name "Your Name"

print("Please enter your Git email. For example, 'your_email@example.com'")
!git config user.email "your_email@example.com"

executed_code_cells = []
for cell_id, cell_data in notebook.items():
    if cell_data['cell_type'] == 'code_cell' and cell_data['execution_status'] != 'not yet executed':
        executed_code_cells.append(cell_data['content'])

concatenated_code = '\n\n'.join(executed_code_cells)

print(f"Extracted {len(executed_code_cells)} executed code cells.")

executed_code_cells = []
for cell in self.notebook.cells:
    if cell['cell_type'] == 'code_cell' and cell.get('execution_status') != 'not yet executed':
        executed_code_cells.append(cell['content'])

concatenated_code = '\n\n'.join(executed_code_cells)

print(f"Extracted {len(executed_code_cells)} executed code cells.")

from IPython import get_ipython

executed_code_cells = []
ipython = get_ipython()

if ipython is not None:
    # Iterate through the history of executed inputs
    # The history_manager.input_hist_raw contains the content of executed code cells
    for cell_content in ipython.history_manager.input_hist_raw:
        executed_code_cells.append(cell_content)

concatenated_code = '\n\n'.join(executed_code_cells)

print(f"Extracted {len(executed_code_cells)} executed code cells.")