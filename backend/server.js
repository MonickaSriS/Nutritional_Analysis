const express = require("express");
const cors = require("cors");
const nutritionRoutes = require("./routes/nutritionRoutes");

const app = express();
app.use(cors());
app.use("/api/nutrition", nutritionRoutes);

app.listen(5000, () => {
  console.log("Backend running on port 5000");
});
