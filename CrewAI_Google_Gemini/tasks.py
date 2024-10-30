from crewai import Task
from tools import tool
from agents import news_researcher,news_writer

#Research Task
research_task=Task(
    description=(
        "Identify the big trend in {topic}."
        "Focus on identifying pros and cons and the overall narrative."
        "Your final report should clearly articulate the key points."
        "its market opportunities, and potential risks."
    ),
    expected_output='A comprehensive 2 paragraphs long report on the latest ai trends.',
    tools=[tool],
    agent=news_researcher,
)

## Writing a task with language model configuration

write_task=Task(
    description=(
        "Compose a insightful article on {topic}."
        "Focus on the latest trends and how it's impacting on the industry."
        "This article should be easy to understand,engaging, and positive."
    ),
    expected_output='Generate the 5 line paragraph article on {topic} advancemets formatted as markdown.',
    tools=[tool],
    agent=news_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)