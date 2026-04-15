const express = require("express");
const multer = require("multer");
const { exec } = require("child_process");
const path = require("path");

const router = express.Router();
const upload = multer({ dest: "uploads/" });

router.post("/analyze", upload.single("receipt"), (req, res) => {
  const imagePath = path.join(__dirname, "..", req.file.path);

  exec(
  `python ../grocery_nutrition_ai/main.py "${imagePath}"`,
  (error, stdout, stderr) => {
    if (error) {
      console.error("EXEC ERROR:", error);
      console.error("STDERR:", stderr);
      return res.status(500).json({
        error: "Python execution failed",
        details: stderr || error.message
      });
    }

    try {
      const data = JSON.parse(stdout);
      res.json(data);
    } catch (parseError) {
      console.error("JSON PARSE ERROR:", stdout);
      res.status(500).json({
        error: "Invalid JSON from Python",
        rawOutput: stdout
      });
    }
  }
);

});

module.exports = router;
