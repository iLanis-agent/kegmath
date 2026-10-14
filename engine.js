(function (root) {
  "use strict";
  var OZ_PER_GAL = 128;      // labeled ounces per gallon
  var KEGS_PER_LB = 1.5;     // labeled half-barrels a pound of CO2 pushes
  var MIN_PER_DEG = 0.75;    // labeled fridge hours per degree F

  function round0(x) { return Math.round(x); }
  function round1(x) { return Math.round(x * 10) / 10; }

  function pourPlan(gal, pourOz) {
    if (!(gal > 0) || !(pourOz > 0)) return { error: "the keg and the pour must be positive" };
    var servings = round0(gal * OZ_PER_GAL / pourOz);
    var verdict;
    if (servings <= 50) verdict = "a small gathering";
    else if (servings <= 100) verdict = "a proper party";
    else verdict = "a serious crowd";
    return { servings: servings, verdict: verdict };
  }

  function gasPlan(lb) {
    if (!(lb > 0)) return { error: "the tank must be positive" };
    var kegs = round1(lb * KEGS_PER_LB);
    var verdict;
    if (kegs < 3) verdict = "a season of weekends";
    else if (kegs <= 8) verdict = "a year of parties";
    else verdict = "a cellar's worth";
    return { kegs: kegs, verdict: verdict };
  }

  function chillPlan(startF, targetF) {
    if (!(targetF < startF)) return { error: "the keg is already at or below the target" };
    var hours = round1((startF - targetF) * MIN_PER_DEG);
    var verdict;
    if (hours <= 6) verdict = "chill this morning";
    else if (hours <= 24) verdict = "chill the day before";
    else verdict = "a two-day promise";
    return { hours: hours, verdict: verdict };
  }

  function renderPour(r, gal, pourOz) {
    return "A " + gal + " gal keg pours " + r.servings + " servings at " + pourOz + " oz - " + r.verdict + ".";
  }

  function renderGas(r, lb) {
    return "A " + lb + " lb CO2 tank pushes about " + r.kegs + " half-barrels - " + r.verdict + ".";
  }

  function renderChill(r, startF, targetF) {
    return "Cooling " + startF + " F to " + targetF + " F needs " + r.hours + " h in the fridge - " + r.verdict + ".";
  }

  var api = { pourPlan: pourPlan, gasPlan: gasPlan, chillPlan: chillPlan, renderPour: renderPour, renderGas: renderGas, renderChill: renderChill };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.KegMath = api;
})(this);
