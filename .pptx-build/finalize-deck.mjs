import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";

const workspaceDir = "/Users/epower/Documents/New project";
const skillDir = "/Users/epower/.codex/plugins/cache/openai-primary-runtime/presentations/26.903.11726/skills/presentations";
const runtimePython = "/Users/epower/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3";
const { finalizePresentation } = await import(pathToFileURL(path.join(skillDir, "container_tools/artifact_tool_utils.mjs")).href);
const result = await finalizePresentation({
  workspaceDir,
  candidatePath: path.join(workspaceDir, ".pptx-build", "bike-sharing-defense-draft.pptx"),
  finalPath: path.join(workspaceDir, ".pptx-output", "共享单车项目答辩演示.pptx"),
  pythonExecutable: runtimePython,
  integrityValidatorPath: path.join(skillDir, "container_tools", "inspect_presentation_package_integrity.py"),
  layoutValidatorPath: path.join(skillDir, "container_tools", "inspect_presentation_layout_geometry.py"),
  layoutArgs: ["--expected-slide-size-emu", "12192000,6858000", "--validate-bullet-geometry", "--validate-heading-fit"],
  requiredNativeChartOwnerSlides: [5],
  materializeLiteralChartWorkbooks: true,
  requiredNativeTableOwnerSlides: [],
  verifyArtifactToolImport: true,
  receiptPath: path.join(workspaceDir, ".codex-finalizer", "presentation-validation.json"),
});
console.log(JSON.stringify(result));
