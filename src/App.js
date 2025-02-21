import React, { useState } from "react";
import axios from "axios";
import { ClipLoader } from "react-spinners";

function App() {
  const [videoUrl, setVideoUrl] = useState("");
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResponse(null);

    try {
      const res = await axios.post("http://localhost:5000/process", {
        video_url: videoUrl,
        query: query
      });
      setResponse(res.data);
    } catch (error) {
      console.error("Error fetching response", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h2>Langchain YouTube Chatbot</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter YouTube URL"
          value={videoUrl}
          onChange={(e) => setVideoUrl(e.target.value)}
        />
        <input
          type="text"
          placeholder="Enter your question"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>

      {/* แสดง animation ตอนกำลังโหลด */}
      {loading ? (
        <div style={{ textAlign: "center", marginTop: "20px" }}>
          <ClipLoader color="#36d7b7" loading={loading} size={50} />
        </div>
      ) : (
        response && (
          <div className="response-container">
            <h3>Response:</h3>
            <p>{response.response}</p>

            <h4>References:</h4>
            {response.references && response.references.length > 0 ? (
              <ul>
                {response.references.map((ref, index) => (
                  <li key={index} className="reference-item">
                    {ref?.content || "No content available"}
                  </li>
                ))}
              </ul>
            ) : (
              <p>No references available</p>
            )}
          </div>
        )
      )}
    </div>
  );
}

export default App;
