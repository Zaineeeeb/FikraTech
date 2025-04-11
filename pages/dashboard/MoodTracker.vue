<template>
  <div class="min-h-screen bg-gray-50 font-sans">
    <NavBar />

    <div class="container mx-auto px-4 py-6">
      <div class="flex flex-col lg:flex-row gap-6">
        <SideBar activeTab="mood" />

        <div class="flex-1">
          <div class="bg-white rounded-xl shadow-sm p-6 mb-6">
            <h1 class="text-2xl font-bold text-gray-900 mb-6">
              Mood Detection
            </h1>

            <!-- Camera Section -->
            <div class="mb-8">
              <div class="flex items-center justify-between mb-4">
                <h2 class="text-lg font-semibold text-gray-900">
                  Facial Expression Analysis
                </h2>
                <div class="flex items-center space-x-2">
                  <button
                    @click="toggleCamera"
                    class="text-sm px-3 py-1 rounded-md flex items-center"
                    :class="
                      isCameraActive
                        ? 'bg-red-100 text-red-600'
                        : 'bg-purple-100 text-purple-600'
                    "
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-4 w-4 mr-1"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        v-if="!isCameraActive"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"
                      />
                      <path
                        v-if="isCameraActive"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M10 9v4a1 1 0 002 0V9a1 1 0 00-2 0z"
                      />
                      <path
                        v-if="isCameraActive"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M5 10h1m13 0h1"
                      />
                    </svg>
                    {{ isCameraActive ? "Stop Camera" : "Start Camera" }}
                  </button>
                  <button
                    @click="captureImage"
                    :disabled="!isCameraActive || isLoading"
                    class="text-sm px-3 py-1 bg-purple-600 text-white rounded-md flex items-center disabled:opacity-50"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-4 w-4 mr-1"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"
                      />
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"
                      />
                    </svg>
                    {{ isLoading ? "Processing..." : "Capture" }}
                  </button>
                  <button
                    @click="audioEnabled = !audioEnabled"
                    class="text-sm px-3 py-1 rounded-md flex items-center"
                    :class="audioEnabled ? 'bg-blue-100 text-blue-600' : 'bg-gray-100 text-gray-600'"
                  >
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path v-if="audioEnabled" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
                      <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z M17 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2" />
                    </svg>
                    {{ audioEnabled ? "Audio On" : "Audio Off" }}
                  </button>
                </div>
              </div>

              <!-- Camera Preview and Results -->
              <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <!-- Camera Feed -->
                <div
                  class="bg-gray-100 rounded-xl overflow-hidden aspect-video relative"
                >
                  <div
                    v-if="!isCameraActive"
                    class="h-full flex flex-col items-center justify-center text-gray-400 p-4 text-center"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-12 w-12 mb-3"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="1"
                        d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"
                      />
                    </svg>
                    <p>Camera is inactive</p>
                    <p class="text-sm mt-1">
                      Click "Start Camera" to begin mood detection
                    </p>
                  </div>
                  <video
                    v-else
                    ref="cameraFeed"
                    autoplay
                    playsinline
                    muted
                    class="w-full h-full object-cover"
                    width="640"
                    height="480"
                  ></video>

                  <!-- Overlay elements for face detection -->
                  <div
                    v-if="isCameraActive && faceDetected"
                    class="absolute inset-0 pointer-events-none"
                  >
                    <div
                      v-for="(face, index) in detectedFaces"
                      :key="index"
                      class="absolute border-2 border-purple-400 rounded-lg"
                      :style="{
                        left: `${face.x}px`,
                        top: `${face.y}px`,
                        width: `${face.width}px`,
                        height: `${face.height}px`,
                      }"
                    >
                      <div class="absolute -top-6 left-0 flex items-center">
                        <span
                          class="text-xs font-medium bg-purple-100 text-purple-800 px-2 py-1 rounded-full"
                        >
                          {{ face.mood || "Analyzing..." }}
                        </span>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Analysis Results -->
                <div class="bg-gray-50 rounded-xl p-4">
                  <div
                    v-if="!lastAnalysis"
                    class="h-full flex flex-col items-center justify-center text-gray-400 p-4 text-center"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-12 w-12 mb-3"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="1"
                        d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"
                      />
                    </svg>
                    <p>No analysis yet</p>
                    <p class="text-sm mt-1">
                      Capture an image to see mood analysis results
                    </p>
                  </div>

                  <div v-else>
                    <div
                      class="p-4 rounded-lg"
                      :class="moodColorClass(lastAnalysis.dominantMood, 'bg')"
                    >
                      <div class="text-4xl text-center mb-2">
                        {{ moodEmoji(lastAnalysis.dominantMood) }}
                      </div>
                      <h3 class="text-xl font-bold text-center">
                        {{ lastAnalysis.dominantMood }}
                      </h3>
                      <p class="text-center mt-1">
                        Confidence: {{ lastAnalysis.confidence.toFixed(1) }}%
                      </p>
                    </div>

                    <div class="mt-4">
                      <h4 class="text-sm font-medium text-gray-700 mb-2">
                        Mood Breakdown
                      </h4>
                      <div class="space-y-2">
                        <div
                          v-for="(score, mood) in lastAnalysis.moodScores"
                          :key="mood"
                          class="flex items-center"
                        >
                          <span class="text-xs w-20">{{ mood }}</span>
                          <div class="flex-1 bg-gray-200 rounded-full h-2 mx-2">
                            <div
                              class="h-full rounded-full"
                              :class="moodColorClass(mood, 'bg')"
                              :style="{ width: `${score}%` }"
                            ></div>
                          </div>
                          <span class="text-xs w-8 text-right"
                            >{{ score.toFixed(1) }}%</span
                          >
                        </div>
                      </div>
                    </div>

                    <div
                      v-if="lastAnalysis?.message"
                      class="mt-4 p-4 bg-purple-50 rounded-lg border border-purple-100"
                    >
                      <div class="flex items-start">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-purple-500 mr-2 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                        </svg>
                        <p class="text-purple-800 italic">
                          "{{ lastAnalysis.message }}"
                        </p>
                      </div>
                    </div>

                    <div
                      class="flex items-center justify-between mt-4 pt-4 border-t border-gray-200"
                    >
                      <span class="text-xs text-gray-500">
                        Analyzed {{ formatTime(lastAnalysis.timestamp) }}
                      </span>
                      <div class="flex space-x-2">
                        <button
                          @click="saveAnalysis"
                          class="text-xs px-3 py-1 bg-purple-600 text-white rounded-md hover:bg-purple-700"
                        >
                          Save Result
                        </button>
                        <button
                          @click="discardAnalysis"
                          class="text-xs px-3 py-1 bg-white border border-gray-300 text-gray-700 rounded-md hover:bg-gray-50"
                        >
                          Discard
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Add this after the camera feed div, but before the API error div -->
              <div 
                v-if="capturedImageUrl" 
                class="mt-4 p-3 bg-gray-50 border border-gray-200 rounded-lg"
              >
                <h3 class="text-sm font-medium text-gray-700 mb-2">Last Captured Image:</h3>
                <div class="bg-white border border-gray-200 rounded-lg overflow-hidden">
                  <img 
                    :src="capturedImageUrl" 
                    alt="Captured image" 
                    class="w-full object-contain max-h-60"
                  />
                </div>
                <p class="text-xs text-gray-500 mt-1">This is the exact image sent to the API</p>
              </div>

              <!-- Add this inside the Camera Preview section, after the camera feed div -->
              <div
                v-if="apiError"
                class="mt-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-600 text-sm"
              >
                <div class="flex items-center">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 mr-2"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                  <span>{{ apiError }}</span>
                </div>
                <button
                  @click="apiError = null"
                  class="mt-2 text-xs px-2 py-1 bg-white border border-red-200 text-red-600 rounded-md hover:bg-red-50"
                >
                  Dismiss
                </button>
              </div>
            </div>

            <!-- Mood History -->
            <div>
              <div class="flex items-center justify-between mb-4">
                <h2 class="text-lg font-semibold text-gray-900">
                  Your Mood History
                </h2>
                <div class="flex space-x-2">
                  <button
                    @click="timeRange = 'week'"
                    class="text-sm px-3 py-1 rounded-md"
                    :class="
                      timeRange === 'week'
                        ? 'bg-purple-100 text-purple-600'
                        : 'text-gray-500 hover:bg-gray-50'
                    "
                  >
                    Week
                  </button>
                  <button
                    @click="timeRange = 'month'"
                    class="text-sm px-3 py-1 rounded-md"
                    :class="
                      timeRange === 'month'
                        ? 'bg-purple-100 text-purple-600'
                        : 'text-gray-500 hover:bg-gray-50'
                    "
                  >
                    Month
                  </button>
                  <button
                    @click="timeRange = 'year'"
                    class="text-sm px-3 py-1 rounded-md"
                    :class="
                      timeRange === 'year'
                        ? 'bg-purple-100 text-purple-600'
                        : 'text-gray-500 hover:bg-gray-50'
                    "
                  >
                    Year
                  </button>
                </div>
              </div>

              <div class="h-64 bg-gray-50 rounded-lg p-4 mb-6">
                <div
                  class="h-full flex items-center justify-center text-gray-400"
                >
                  Mood chart visualization for {{ timeRange }}
                </div>
              </div>

              <h3 class="text-sm font-medium text-gray-700 mb-3">
                Recent Mood Logs
              </h3>
              <div class="space-y-3">
                <div
                  v-for="log in moodHistory"
                  :key="log.id"
                  class="p-3 bg-gray-50 rounded-lg flex items-center"
                >
                  <div
                    class="flex-shrink-0 h-10 w-10 rounded-full flex items-center justify-center text-2xl mr-3"
                    :class="moodColorClass(log.mood, 'bg')"
                  >
                    {{ moodEmoji(log.mood) }}
                  </div>
                  <div class="flex-1">
                    <div class="flex items-center justify-between">
                      <span class="font-medium">{{ log.mood }}</span>
                      <span class="text-xs text-gray-500">{{
                        formatTime(log.timestamp)
                      }}</span>
                    </div>
                    <div class="text-sm text-gray-600 mt-1">
                      Confidence: {{ log.confidence }}%
                      <span v-if="log.note" class="ml-2">• {{ log.note }}</span>
                    </div>
                  </div>
                </div>

                <div
                  v-if="moodHistory.length === 0"
                  class="text-center py-6 text-gray-400"
                >
                  No mood logs yet. Start using the camera to track your moods.
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, nextTick } from "vue";

interface MoodAnalysis {
  dominantMood: string;
  confidence: number;
  moodScores: Record<string, number>;
  timestamp: Date;
  message?: string;
}

interface MoodLog {
  id: number;
  mood: string;
  confidence: number;
  timestamp: Date;
  note?: string;
}

interface FaceDetection {
  x: number;
  y: number;
  width: number;
  height: number;
  mood?: string;
}

// API configuration
const API_URL = import.meta.env.VITE_API_URL || "https://hackathon-456421.uc.r.appspot.com";
const API_ENDPOINTS = {
  predict: `${API_URL}/predict`,
  history: `${API_URL}/history`,
};

// State
const isCameraActive = ref(false);
const cameraFeed = ref<HTMLVideoElement | null>(null);
const faceDetected = ref(false);
const detectedFaces = ref<FaceDetection[]>([]);
const lastAnalysis = ref<MoodAnalysis | null>(null);
const timeRange = ref("week");
const isLoading = ref(false);
const apiError = ref<string | null>(null);
const moodHistory = ref<MoodLog[]>([]);
const capturedImageUrl = ref<string | null>(null);
const audioEnabled = ref(true);
const isPlayingAudio = ref(false);
const audioPlayer = ref<HTMLAudioElement | null>(null);

// Mood configuration
const moods = {
  happy: { emoji: "😊", color: "text-green-500", bg: "bg-green-100" },
  neutral: { emoji: "😐", color: "text-blue-500", bg: "bg-blue-100" },
  sad: { emoji: "😔", color: "text-yellow-500", bg: "bg-yellow-100" },
  anxious: { emoji: "😰", color: "text-orange-500", bg: "bg-orange-100" },
  angry: { emoji: "😡", color: "text-red-500", bg: "bg-red-100" },
  fear: { emoji: "😨", color: "text-purple-500", bg: "bg-purple-100" },
  disgust: { emoji: "🤢", color: "text-green-600", bg: "bg-green-200" },
  surprise: { emoji: "😲", color: "text-pink-500", bg: "bg-pink-100" },
};

// Camera control
const toggleCamera = async () => {
  if (isCameraActive.value) {
    stopCamera();
  } else {
    await startCamera();
  }
};

const startCamera = async () => {
  try {
    // Set isCameraActive first, so the video element renders
    isCameraActive.value = true;

    // Wait a tick for Vue to update the DOM
    await nextTick();

    const stream = await navigator.mediaDevices.getUserMedia({
      video: {
        width: { ideal: 640 },
        height: { ideal: 480 },
        facingMode: "user",
      },
    });

    if (cameraFeed.value) {
      cameraFeed.value.srcObject = stream;
      await cameraFeed.value.play();
    } else {
      // If the video element still isn't available, revert the state
      isCameraActive.value = false;
      throw new Error("Camera element not found in DOM");
    }
  } catch (error) {
    console.error("Camera error:", error);
    isCameraActive.value = false;
    alert(
      `Could not access camera: ${
        error instanceof Error ? error.message : "Unknown error"
      }`
    );
  }
};

const stopCamera = () => {
  if (cameraFeed.value?.srcObject) {
    const stream = cameraFeed.value.srcObject as MediaStream;
    stream.getTracks().forEach((track) => track.stop());
  }
  isCameraActive.value = false;
  faceDetected.value = false;
  detectedFaces.value = [];
};

// Image capture and analysis
const captureImage = async () => {
  if (!isCameraActive.value || !cameraFeed.value || isLoading.value) return;

  isLoading.value = true;
  faceDetected.value = false;
  apiError.value = null;
  capturedImageUrl.value = null; // Reset previous capture

  try {
    const canvas = document.createElement("canvas");
    const video = cameraFeed.value;
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const ctx = canvas.getContext("2d");

    if (!ctx) throw new Error("Could not get canvas context");

    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    
    // Save the image URL for display
    capturedImageUrl.value = canvas.toDataURL("image/jpeg");

    const blob = await new Promise<Blob | null>((resolve) => {
      canvas.toBlob(resolve, "image/jpeg", 0.9);
    });

    if (!blob) throw new Error("Failed to create image blob");
    
    console.log("Sending image to API, size:", Math.round(blob.size / 1024), "KB");

    const formData = new FormData();
    formData.append("file", blob, "capture.jpg");

    const response = await fetch(API_ENDPOINTS.predict, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`API request failed: ${response.status} - ${errorText}`);
    }

    const data = await response.json();
    console.log("Mood API response:", data);

    // Handle the API response format from FastAPI
    if (data.error) {
      throw new Error(data.error);
    }

    // Process the detected faces and emotions
    if (data.faces && data.faces.length > 0) {
      processDetectedFaces(data.faces, canvas.width, canvas.height);
    } else if (data.emotion) {
      // Legacy API format support
      lastAnalysis.value = {
        dominantMood: data.emotion,
        confidence: data.confidence || 0,
        moodScores: data.scores || {},
        timestamp: new Date(),
        message: data.message,
      };

      // Play audio for the detected mood
      playMoodAudio(data.emotion);

      // Create a mock face detection if the API doesn't provide face coordinates
      updateFaceDetection(data.emotion, canvas.width, canvas.height);
    } else {
      throw new Error("No faces detected in the image");
    }
  } catch (error) {
    console.error("Error in captureImage:", error);
    apiError.value =
      error instanceof Error ? error.message : "Unknown error occurred";

    // Only use mock data in development mode
    if (import.meta.env.DEV) {
      lastAnalysis.value = getMockAnalysis();
      updateFaceDetection(lastAnalysis.value.dominantMood, 640, 480);
    }
  } finally {
    isLoading.value = false;
  }
};

// Add a function to process detected faces from the API
const processDetectedFaces = (
  faces: any[],
  canvasWidth: number,
  canvasHeight: number
) => {
  detectedFaces.value = faces.map((face) => {
    // Normalize coordinates to match the video element dimensions
    return {
      x: (face.bbox.x / face.image_width) * canvasWidth,
      y: (face.bbox.y / face.image_height) * canvasHeight,
      width: (face.bbox.width / face.image_width) * canvasWidth,
      height: (face.bbox.height / face.image_height) * canvasHeight,
      mood: face.emotion,
    };
  });

  faceDetected.value = detectedFaces.value.length > 0;

  // Use the first face for the main analysis display
  if (detectedFaces.value.length > 0) {
    const primaryFace = faces[0];

    lastAnalysis.value = {
      dominantMood: primaryFace.emotion,
      confidence: primaryFace.confidence || 0,
      moodScores: primaryFace.scores || {},
      timestamp: new Date(),
      message: primaryFace.message,
    };
  }
};

const getMockAnalysis = (): MoodAnalysis => {
  const emotions = ["Happy", "Sad", "Neutral", "Angry", "Surprise"];
  const randomMood = emotions[Math.floor(Math.random() * emotions.length)];

  return {
    dominantMood: randomMood,
    confidence: Math.random() * 50 + 50, // 50-100%
    moodScores: {
      Angry: Math.random() * 100,
      Disgust: Math.random() * 100,
      Fear: Math.random() * 100,
      Happy: Math.random() * 100,
      Sad: Math.random() * 100,
      Surprise: Math.random() * 100,
      Neutral: Math.random() * 100,
    },
    timestamp: new Date(),
    message: "You matter. And even if you can't feel it now, your happiness matters too.",
  };
};

// Helper functions
const moodColorClass = (mood: string, type: string = "text"): string => {
  const moodKey = mood.toLowerCase() as keyof typeof moods;
  return (
    moods[moodKey]?.[type as keyof (typeof moods)[typeof moodKey]] ||
    (type === "text" ? "text-gray-500" : "bg-gray-100")
  );
};

const moodEmoji = (mood: string): string => {
  const moodKey = mood.toLowerCase() as keyof typeof moods;
  return moods[moodKey]?.emoji || "❓";
};

const formatTime = (date: Date): string => {
  return date.toLocaleString("en-US", {
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
};

const saveAnalysis = async () => {
  if (!lastAnalysis.value) return;

  // Store values locally to prevent null reference issues
  const moodData = {
    mood: lastAnalysis.value.dominantMood,
    confidence: lastAnalysis.value.confidence,
    timestamp: lastAnalysis.value.timestamp,
  };

  isLoading.value = true;
  apiError.value = null;

  try {
    // Create a new mood log entry
    const newLog = {
      mood: moodData.mood,
      confidence: moodData.confidence,
      timestamp: moodData.timestamp.toISOString(),
      scores: lastAnalysis.value.moodScores,
      note: "Camera detection",
    };

    // Send the mood log to the API if endpoint exists
    const response = await fetch(API_ENDPOINTS.history, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newLog),
    });

    if (!response.ok) {
      throw new Error(`Failed to save mood analysis: ${response.status}`);
    }

    // Add to local history
    moodHistory.value.unshift({
      id: Date.now(),
      mood: moodData.mood,
      confidence: moodData.confidence,
      timestamp: moodData.timestamp,
      note: "Camera detection",
    });

    lastAnalysis.value = null;
  } catch (error) {
    console.error("Error saving analysis:", error);
    apiError.value =
      error instanceof Error ? error.message : "Failed to save mood data";

    // Still add to local history even if API fails
    moodHistory.value.unshift({
      id: Date.now(),
      mood: moodData.mood,
      confidence: moodData.confidence,
      timestamp: moodData.timestamp,
      note: "Camera detection (local only)",
    });

    lastAnalysis.value = null;
  } finally {
    isLoading.value = false;
  }
};

const discardAnalysis = () => {
  lastAnalysis.value = null;
};

// Add a function to fetch mood history from the API
const fetchMoodHistory = async () => {
  try {
    const response = await fetch(API_ENDPOINTS.history);

    if (!response.ok) {
      throw new Error(`Failed to fetch mood history: ${response.status}`);
    }

    const data = await response.json();

    // Convert API response to our format
    moodHistory.value = data.map((item: any) => ({
      id: item.id || Date.now(),
      mood: item.mood,
      confidence: item.confidence,
      timestamp: new Date(item.timestamp),
      note: item.note || "API data",
    }));
  } catch (error) {
    console.error("Error fetching mood history:", error);
    // Fall back to mock data if in development mode
    if (import.meta.env.DEV) {
      loadMockHistory();
    }
  }
};

// Rename the existing mock history loading to be more explicit
const loadMockHistory = () => {
  moodHistory.value = [
    {
      id: 1,
      mood: "Happy",
      confidence: 85,
      timestamp: new Date(Date.now() - 3600000),
      note: "Morning check-in",
    },
    {
      id: 2,
      mood: "Neutral",
      confidence: 72,
      timestamp: new Date(Date.now() - 86400000),
      note: "After work",
    },
    {
      id: 3,
      mood: "Sad",
      confidence: 68,
      timestamp: new Date(Date.now() - 2 * 86400000),
      note: "Before meeting",
    },
  ];
};

// Update the onMounted hook to fetch real data if available
onMounted(() => {
  // Try to fetch real mood history from API
  fetchMoodHistory();

  // Add event listener for video element
  if (cameraFeed.value) {
    cameraFeed.value.addEventListener("loadedmetadata", () => {
      console.log(
        "Video dimensions ready:",
        cameraFeed.value?.videoWidth,
        cameraFeed.value?.videoHeight
      );
    });
  }
});

// Clean up camera on unmount
onUnmounted(() => {
  stopCamera();
});

// Add this function alongside your other functions
const updateFaceDetection = (mood: string, width: number, height: number) => {
  faceDetected.value = true;
  detectedFaces.value = [
    {
      x: width / 2 - 60,
      y: height / 2 - 60,
      width: 120,
      height: 120,
      mood: mood,
    },
  ];
};

// Add this function to play mood-specific audio
const playMoodAudio = async (mood: string) => {
  if (!audioEnabled.value || isPlayingAudio.value) return;
  
  try {
    isPlayingAudio.value = true;
    const moodKey = mood.toLowerCase();
    const audioUrl = `${import.meta.env.VITE_GCP_BUCKET_URL || 'https://storage.googleapis.com/mood-audios'}/${moodKey}.wav`;
    
    console.log(`Playing mood audio for: ${mood}`, audioUrl);
    
    if (!audioPlayer.value) {
      audioPlayer.value = new Audio();
    }
    
    audioPlayer.value.src = audioUrl;
    audioPlayer.value.onended = () => {
      isPlayingAudio.value = false;
    };
    
    await audioPlayer.value.play();
  } catch (error) {
    console.error('Error playing mood audio:', error);
    isPlayingAudio.value = false;
  }
};
</script>

<style scoped>
/* Additional styles if needed */
</style>
