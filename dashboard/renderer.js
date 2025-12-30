const fs = require("fs");
const path = require("path");

const DATA_PATH = path.join(__dirname, "../data/sessions.json");

// read data
let data = [];
try {
  data = JSON.parse(fs.readFileSync(DATA_PATH, "utf-8"));
} catch (e) {
  console.error("Failed to read JSON:", e);
}

// ---------- SHOW JSON ----------
document.getElementById("jsonView").textContent =
  JSON.stringify(data, null, 2);

// ---------- FOCUS SCORE GRAPH ----------
const focusLabels = data.map(d => d.timestamp);
const focusScores = data.map(d => d.focus_score || d.focus_score === 0 ? d.focus_score : d.focus_score);

new Chart(document.getElementById("focusChart"), {
  type: "line",
  data: {
    labels: focusLabels,
    datasets: [{
      label: "Focus Score",
      data: focusScores,
      borderColor: "#7c7cff",
      tension: 0.3
    }]
  }
});

// ---------- APP USAGE GRAPH (LAST SESSION) ----------
if (data.length > 0) {
  const lastSession = data[data.length - 1];
  const apps = Object.keys(lastSession.app_usage_seconds || {});
  const appTimes = Object.values(lastSession.app_usage_seconds || {});

  new Chart(document.getElementById("appChart"), {
    type: "bar",
    data: {
      labels: apps,
      datasets: [{
        label: "Seconds Used",
        data: appTimes,
        backgroundColor: "#ff9800"
      }]
    }
  });
}
