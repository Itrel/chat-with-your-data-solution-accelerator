from azure.monitor.opentelemetry import configure_azure_monitor

configure_azure_monitor()

# httpx is used by openai
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor  # noqa: E402

HTTPXClientInstrumentor().instrument()

from create_app import create_app  # noqa: E402

app = create_app()

if __name__ == "__main__":
    app.run()
