import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "../../api/axios";

export const sendMessage = createAsyncThunk(
  "chat/sendMessage",
  async (message, { getState, rejectWithValue }) => {
    try {
      const state = getState().chat;

      const response = await axios.post("/chat", {
        message,
        thread_id: "test-001",
        form_state: state.formState,
      });

      return {
        userMessage: message,
        assistantMessage: response.data.assistant_message,
        formState: response.data.form_state,
      };
    } catch (err) {
      return rejectWithValue(
        err.response?.data?.detail ||
        err.message ||
        "Something went wrong."
      );
    }
  }
);

const initialState = {
  messages: [],
  loading: false,
  error: null,

  formState: {
    id: "",
    hcp_name: "",
    interaction_type: "",
    interaction_date: "",
    interaction_time: "",
    attendees: "",
    summary: "",
    materials_shared: "",
    samples_distributed: "",
    sentiment: "",
    outcomes: "",
    compliance_status: "",
    next_best_action: "",
  },
};

const chatSlice = createSlice({
  name: "chat",

  initialState,

  reducers: {
    clearChat(state) {
      state.messages = [];
      state.error = null;
      state.formState = initialState.formState;
    },
  },

  extraReducers: (builder) => {
    builder

      .addCase(sendMessage.pending, (state) => {
        state.loading = true;
        state.error = null;
      })

      .addCase(sendMessage.fulfilled, (state, action) => {
        state.loading = false;

        state.messages.push({
          role: "user",
          content: action.payload.userMessage,
        });

        state.messages.push({
          role: "assistant",
          content: action.payload.assistantMessage,
        });

        state.formState = {
          ...state.formState,
          ...(action.payload.formState || {}),
        };
      })

      .addCase(sendMessage.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  },
});

export const { clearChat } = chatSlice.actions;

export default chatSlice.reducer;