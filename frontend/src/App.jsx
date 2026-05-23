import { useState } from "react"
import axios from "axios"

function App() {

  const [file, setFile] = useState(null)

  const [jobDescription, setJobDescription] = useState("")

  const [result, setResult] = useState(null)

  const [jobs, setJobs] = useState([])

  const [loading, setLoading] = useState(false)


  const handleSubmit = async () => {

    if (!file) {

      alert("Please upload resume")

      return
    }

    const formData = new FormData()

    formData.append("file", file)

    try {

      setLoading(true)

      // Resume Analysis
      const response = await axios.post(

        "https://ai-career-assistant-mudy.onrender.com/analyze",

        formData
      )

      setResult(response.data)


      // Recommended Jobs
      const jobsResponse = await axios.post(

        "https://ai-career-assistant-mudy.onrender.com/recommend-jobs",

        formData
      )

      setJobs(jobsResponse.data)

    }

    catch (error) {

      console.log(error)

      alert("Error analyzing resume")
    }

    finally {

      setLoading(false)
    }
  }


  return (

    <div
      style={{
        backgroundColor: "#0f172a",
        minHeight: "100vh",
        color: "white",
        padding: "40px",
        fontFamily: "Arial"
      }}
    >

      <h1
        style={{
          textAlign: "center",
          fontSize: "50px",
          color: "#22d3ee",
          marginBottom: "40px"
        }}
      >

        AI Career Assistant

      </h1>


      {/* Upload Section */}

      <div
        style={{
          maxWidth: "800px",
          margin: "auto",
          backgroundColor: "#1e293b",
          padding: "30px",
          borderRadius: "20px"
        }}
      >

        <input

          type="file"

          accept=".pdf"

          onChange={(e) => setFile(e.target.files[0])}

          style={{
            marginBottom: "20px"
          }}
        />

        <textarea

          placeholder="Optional Job Description..."

          value={jobDescription}

          onChange={(e) =>
            setJobDescription(e.target.value)
          }

          style={{
            width: "100%",
            height: "150px",
            padding: "15px",
            borderRadius: "10px",
            fontSize: "16px"
          }}
        />

        <br />
        <br />

        <button

          onClick={handleSubmit}

          style={{
            backgroundColor: "#06b6d4",
            color: "white",
            padding: "12px 25px",
            border: "none",
            borderRadius: "10px",
            fontSize: "18px",
            cursor: "pointer",
            fontWeight: "bold"
          }}
        >

          {loading ? "Analyzing..." : "Analyze Resume"}

        </button>

      </div>


      {/* Analysis Result */}

      {result && (

        <div
          style={{
            maxWidth: "800px",
            margin: "40px auto",
            backgroundColor: "#1e293b",
            padding: "30px",
            borderRadius: "20px"
          }}
        >

          <h2 style={{ color: "#22d3ee" }}>

            Analysis Result

          </h2>

          <h3>

            ATS Score:
            <span style={{ color: "#22d3ee" }}>

              {" "} {result.ats_score}

            </span>

          </h3>

          <h3>

            Match Score:
            <span style={{ color: "#4ade80" }}>

              {" "} {result.match_score}

            </span>

          </h3>

          <p>

            <b>Explanation:</b>

            {" "}

            {result.explanation}

          </p>


          {/* Matched Skills */}

          <h3 style={{ color: "#4ade80" }}>

            Matched Skills

          </h3>

          <div>

            {result.matched_skills.map((skill, index) => (

              <span

                key={index}

                style={{
                  backgroundColor: "green",
                  padding: "8px 15px",
                  borderRadius: "20px",
                  marginRight: "10px",
                  display: "inline-block",
                  marginBottom: "10px"
                }}
              >

                {skill}

              </span>
            ))}

          </div>


          {/* Missing Skills */}

          <h3 style={{ color: "#f87171" }}>

            Missing Skills

          </h3>

          <div>

            {result.missing_skills.map((skill, index) => (

              <span

                key={index}

                style={{
                  backgroundColor: "red",
                  padding: "8px 15px",
                  borderRadius: "20px",
                  marginRight: "10px",
                  display: "inline-block",
                  marginBottom: "10px"
                }}
              >

                {skill}

              </span>
            ))}

          </div>

        </div>
      )}


      {/* Recommended Jobs */}

      {jobs.length > 0 && (

        <div
          style={{
            maxWidth: "800px",
            margin: "40px auto",
            backgroundColor: "#1e293b",
            padding: "30px",
            borderRadius: "20px"
          }}
        >

          <h2 style={{ color: "#22d3ee" }}>

            Recommended Jobs

          </h2>

          {jobs.map((job, index) => (

            <div

              key={index}

              style={{
                backgroundColor: "#334155",
                padding: "20px",
                borderRadius: "15px",
                marginBottom: "20px"
              }}
            >

              <h3>

                {job.title}

              </h3>

              <p>

                <b>Company:</b> {job.company}

              </p>

              <p>

                <b>Location:</b> {job.location}

              </p>
              


              <a

                href={job.redirect_url}

                target="_blank"

                rel="noopener noreferrer"

                style={{
                  display: "inline-block",
                  marginTop: "10px",
                  backgroundColor: "#06b6d4",
                  color: "white",
                  padding: "10px 18px",
                  borderRadius: "10px",
                  textDecoration: "none",
                  fontWeight: "bold"
                }}
              >

                Apply Now →

              </a>


              <p style={{ marginTop: "15px" }}>

                <b>Match Score:</b>

                <span
                  style={{
                    color: "#4ade80"
                  }}
                >

                  {" "} {job.match_score}%

                </span>

              </p>

            </div>
          ))}

        </div>
      )}

    </div>
  )
}

export default App