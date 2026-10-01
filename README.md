# Version Hub

Version Hub is a small FastAPI service for tracking and incrementing project
versions. Project data is stored in MongoDB, and the API is protected with
HTTP Basic Authentication.

## Requirements

- Python 3.12 or newer
- A MongoDB database

## Configuration

Create a `.env` file in the project root:

```env
MONGO_DB_URI=mongodb+srv://<username>:<password>@<cluster>/<database>
MONGO_DB_NAME=version_hub
API_USERNAME=your-api-username
API_PASSWORD=your-api-password
```

## Run locally

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API is available at `http://localhost:8000`. Interactive documentation is
available at `http://localhost:8000/docs`.

## API

Check the service health:

```bash
curl http://localhost:8000/health
```

Read a project's version:

```bash
curl -u "your-api-username:your-api-password" \
	http://localhost:8000/projects/test-project/version
```

Increment a project's version:

```bash
curl -X POST \
	-u "your-api-username:your-api-password" \
	http://localhost:8000/projects/test-project/version
```

The project must already exist in the `projects` collection with a document
similar to:

```json
{
	"project_name": "test-project",
	"current_version": 1
}
```

## Deploy to Vercel

The included `vercel.json` configures Vercel to use `app/main.py` as the
FastAPI entrypoint.

1. Import this repository into Vercel.
2. Add `MONGO_DB_URI`, `MONGO_DB_NAME`, `API_USERNAME`, and `API_PASSWORD` as
	 Vercel environment variables.
3. Deploy the project.

After deployment, use the generated Vercel URL in place of
`http://localhost:8000`.
