<template>
  <div class="min-h-screen bg-gray-50 font-sans">
    <!-- Reuse the same navigation from Dashboard -->
    <NavBar />

    <div class="container mx-auto px-4 py-6">
      <div class="flex flex-col lg:flex-row gap-6">
        <!-- Reuse the sidebar -->
        <SideBar activeTab="journal" />

        <!-- Journal-specific content -->
        <div class="flex-1">
          <div class="bg-white rounded-xl shadow-sm p-6 mb-6">
            <div class="flex items-center justify-between mb-6">
              <h1 class="text-2xl font-bold text-gray-900">Journal</h1>
              <button
                @click="createNewEntry"
                class="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 flex items-center"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 mr-1"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M12 4v16m8-8H4"
                  />
                </svg>
                New Entry
              </button>
            </div>

            <!-- Journal entries list -->
            <div class="space-y-4">
              <div
                v-for="entry in entries"
                :key="entry.id"
                class="border border-gray-200 rounded-lg p-5 hover:shadow-md transition-shadow cursor-pointer"
                @click="viewEntry(entry.id)"
              >
                <div class="flex justify-between items-start mb-2">
                  <h3 class="text-lg font-medium text-gray-900">
                    {{ entry.title }}
                  </h3>
                  <span class="text-sm text-gray-500">{{
                    formatDate(entry.date)
                  }}</span>
                </div>
                <p class="text-gray-600 mb-3">{{ entry.preview }}</p>
                <div class="flex space-x-2">
                  <span
                    v-for="tag in entry.tags"
                    :key="tag"
                    class="text-xs px-2 py-1 bg-purple-50 text-purple-600 rounded-full"
                  >
                    {{ tag }}
                  </span>
                </div>
              </div>

              <!-- Empty state -->
              <div v-if="entries.length === 0" class="text-center py-12">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-16 w-16 mx-auto text-gray-300"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="1"
                    d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                  />
                </svg>
                <h3 class="mt-4 text-lg font-medium text-gray-900">
                  No journal entries yet
                </h3>
                <p class="mt-1 text-gray-500">
                  Start writing to reflect on your thoughts and feelings
                </p>
                <button
                  @click="createNewEntry"
                  class="mt-6 bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 flex items-center mx-auto"
                >
                  Create your first entry
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
// import NavBar from "../components/NavBar.vue";
// import SideBar from "../components/SideBar.vue";

const entries = ref([
  {
    id: 1,
    title: "Morning Reflection",
    preview:
      "Today I woke up feeling refreshed and ready to take on the day...",
    date: new Date(),
    tags: ["morning", "reflection"],
  },
  {
    id: 2,
    title: "Work Stress",
    preview:
      "The project deadline is approaching and I feel the pressure building up...",
    date: new Date(Date.now() - 86400000),
    tags: ["work", "stress"],
  },
  {
    id: 3,
    title: "Gratitude Entry",
    preview:
      "I am grateful for my supportive friends who checked in on me today...",
    date: new Date(Date.now() - 2 * 86400000),
    tags: ["gratitude", "friends"],
  },
]);

const formatDate = (date) => {
  return date.toLocaleDateString("en-US", {
    month: "short",
    day: "numeric",
    year: "numeric",
  });
};

const createNewEntry = () => {
  // Navigate to new entry page or open modal
  console.log("Create new journal entry");
};

const viewEntry = (id) => {
  // Navigate to entry detail page
  console.log(`View journal entry ${id}`);
};
</script>
