import taipy.gui as gui
import pandas as pd
import os

CSV_PATH = os.path.join("data", "beneficiaries.csv")

def load_data():
    return pd.read_csv(CSV_PATH)

def save_data(df):
    df.to_csv(CSV_PATH, index=False)

def add_beneficiary(row):
    df = load_data()
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    save_data(df)
    return df

def update_beneficiary(index, row):
    df = load_data()
    for col in row:
        df.at[index, col] = row[col]
    save_data(df)
    return df

def delete_beneficiary(index):
    df = load_data()
    df = df.drop(index).reset_index(drop=True)
    save_data(df)
    return df

def get_empty_row():
    df = load_data()
    return {col: "" for col in df.columns}

data = load_data()
selected_idx = -1
form_data = get_empty_row()

def on_add(state):
    global data, form_data
    data = add_beneficiary(form_data)
    state.data = data
    state.form_data = get_empty_row()

def on_update(state):
    global data, form_data, selected_idx
    if selected_idx >= 0:
        data = update_beneficiary(selected_idx, form_data)
        state.data = data
        state.form_data = get_empty_row()
        state.selected_idx = -1

def on_delete(state):
    global data, selected_idx
    if selected_idx >= 0:
        data = delete_beneficiary(selected_idx)
        state.data = data
        state.form_data = get_empty_row()
        state.selected_idx = -1

def on_select(state, idx):
    global data, form_data, selected_idx
    selected_idx = idx
    state.form_data = data.iloc[idx].to_dict()
    state.selected_idx = idx

page_md = (
    "# Beneficiaries CRUD\n\n"
    "<|{data}|table|on_row_click=on_select|width=100%|>\n\n"
    "## Add / Edit Beneficiary\n"
    "<|form_data|input|columns=3|>\n"
    "<|Add|button|on_action=on_add|> "
    "<|Update|button|on_action=on_update|> "
    "<|Delete|button|on_action=on_delete|>"
)

pages = {"/": page_md}
app = gui.Gui(pages=pages)

if __name__ == "__main__":
    app.run(title="Beneficiaries CRUD App", use_reloader=True)
