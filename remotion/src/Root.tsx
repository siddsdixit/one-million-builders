import React from "react";
import { Composition } from "remotion";
import { GitHubHero } from "./GitHubHero";

export function Root() {
  return (
    <Composition
      id="GitHubHero"
      component={GitHubHero}
      durationInFrames={960}
      fps={30}
      width={1200}
      height={630}
      defaultProps={{}}
    />
  );
}
