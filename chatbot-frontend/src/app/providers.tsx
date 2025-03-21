"use client"; 

import { MantineProvider, MantineThemeOverride } from "@mantine/core";
import { Notifications } from "@mantine/notifications";
import React from "react";


const theme: MantineThemeOverride = {
  primaryColor: "blue",
  components: {
    Button: { defaultProps: { size: "md" } },
    TextInput: { defaultProps: { size: "md" } },
  },
};

export function AppProviders({ children }: { children: React.ReactNode }) {
  return (
      <MantineProvider theme={theme}>
        <Notifications position="top-right" />
        {children}
      </MantineProvider>
  );
}
