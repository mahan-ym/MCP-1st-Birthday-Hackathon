import gradio as gr


def process_postcode(postCode, country):
    # Dummy implementation for demonstration purposes
    return f"Processed postcode: {postCode}"


demo = gr.Interface(
    title="Let Me Handle That Grocery List",
    fn=process_postcode,
    theme=gr.themes.Default(
        primary_hue="blue",
        secondary_hue="green",
    ),
    inputs=[
        gr.Textbox(
            label="Enter your postcode",
            placeholder="e.g., 12345",
        ),
        gr.Textbox(
            label="country",
            placeholder="e.g., Italy",
        ),
        gr.Textbox(
            label="Grocery List",
            placeholder="e.g., milk, eggs, bread",
        ),
    ],
    outputs=gr.Textbox(
        label="Result",
    ),
)

if __name__ == "__main__":
    demo.launch(mcp_server=True, max_file_size="15mb")
