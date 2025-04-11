<template>
  <div class="min-h-screen bg-gray-50 font-sans">
    <!-- Dashboard Navigation -->
    <nav class="bg-white shadow-sm sticky top-0 z-10">
      <div
        class="container mx-auto px-4 py-3 flex justify-between items-center"
      >
        <div class="flex items-center space-x-2">
          <svg
            class="h-8 w-8 text-purple-600"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M12 2C6.477 2 2 6.477 2 12C2 17.523 6.477 22 12 22C17.523 22 22 17.523 22 12C22 6.477 17.523 2 12 2ZM12 20C7.582 20 4 16.418 4 12C4 7.582 7.582 4 12 4C16.418 4 20 7.582 20 12C20 16.418 16.418 20 12 20Z"
              fill="currentColor"
            />
            <path
              d="M12 6C8.686 6 6 8.686 6 12C6 15.314 8.686 18 12 18C15.314 18 18 15.314 18 12C18 8.686 15.314 6 12 6ZM12 16C9.791 16 8 14.209 8 12C8 9.791 9.791 8 12 8C14.209 8 16 9.791 16 12C16 14.209 14.209 16 12 16Z"
              fill="currentColor"
            />
            <path
              d="M12 10C10.895 10 10 10.895 10 12C10 13.105 10.895 14 12 14C13.105 14 14 13.105 14 12C14 10.895 13.105 10 12 10Z"
              fill="currentColor"
            />
          </svg>
          <div>
            <h1 class="text-xl font-bold text-gray-800">FikraTech</h1>
            <p class="text-xs text-gray-500">Mental Wellness Dashboard</p>
          </div>
        </div>
        <div class="flex items-center space-x-4">
          <button
            @click="showNotifications"
            class="p-2 text-gray-500 hover:text-purple-600 relative"
            aria-label="Notifications"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
              />
            </svg>
            <span
              v-if="unreadNotifications"
              class="absolute top-0 right-0 h-3 w-3 bg-red-500 rounded-full"
            ></span>
          </button>

          <!-- Notification dropdown -->
          <div class="relative">
            <transition
              enter-active-class="transition ease-out duration-100"
              enter-from-class="transform opacity-0 scale-95"
              enter-to-class="transform opacity-100 scale-100"
              leave-active-class="transition ease-in duration-75"
              leave-from-class="transform opacity-100 scale-100"
              leave-to-class="transform opacity-0 scale-95"
            >
              <div
                v-if="showNotificationDropdown"
                class="absolute right-0 mt-1 w-80 bg-white rounded-lg shadow-xl z-50 ring-1 ring-black ring-opacity-5 overflow-hidden"
                style="max-height: 70vh; top: 100%"
              >
                <!-- Header -->
                <div
                  class="px-4 py-3 border-b border-gray-100 bg-gray-50 flex justify-between items-center sticky top-0 z-10"
                >
                  <p class="text-sm font-medium text-gray-700">Notifications</p>
                  <button
                    @click="markAllAsRead"
                    class="text-xs text-purple-600 hover:text-purple-700 font-medium"
                  >
                    Mark all as read
                  </button>
                </div>

                <!-- Notification List with scroll -->
                <div
                  class="divide-y divide-gray-100 overflow-y-auto"
                  style="max-height: calc(70vh - 80px)"
                >
                  <div
                    v-for="(message, index) in positiveMessages"
                    :key="index"
                    class="px-4 py-3 hover:bg-gray-50 transition-colors cursor-pointer flex items-start"
                    :class="{ 'bg-purple-50': index === 0 }"
                  >
                    <div class="flex-shrink-0 mt-0.5">
                      <div
                        class="h-8 w-8 rounded-full bg-purple-100 flex items-center justify-center text-purple-600"
                      >
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          class="h-4 w-4"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                        >
                          <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                          />
                        </svg>
                      </div>
                    </div>
                    <div class="ml-3 flex-1">
                      <p class="text-sm font-medium text-gray-900">
                        {{ message }}
                      </p>
                      <div class="mt-1 flex justify-between items-center">
                        <p class="text-xs text-gray-500">
                          {{ formatTime(lastNotificationTime) }}
                        </p>
                        <span
                          v-if="index === 0"
                          class="inline-flex items-center px-2 py-0.5 rounded-full text-xs font-medium bg-purple-100 text-purple-800"
                        >
                          New
                        </span>
                      </div>
                    </div>
                  </div>

                  <!-- Empty state -->
                  <div
                    v-if="positiveMessages.length === 0"
                    class="px-4 py-6 text-center"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-12 w-12 mx-auto text-gray-300"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="1"
                        d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
                      />
                    </svg>
                    <p class="mt-2 text-sm text-gray-500">
                      No new notifications
                    </p>
                  </div>
                </div>

                <!-- Footer -->
                <div
                  class="px-4 py-2 border-t border-gray-100 bg-gray-50 text-center sticky bottom-0"
                >
                  <a
                    href="#"
                    class="text-xs font-medium text-purple-600 hover:text-purple-700"
                  >
                    View all notifications
                  </a>
                </div>
              </div>
            </transition>
          </div>

          <div class="relative">
            <button
              @click="toggleUserDropdown"
              class="flex items-center space-x-2 focus:outline-none"
              aria-label="User menu"
            >
              <div
                class="w-8 h-8 rounded-full bg-purple-100 flex items-center justify-center text-purple-600 font-medium"
              >
                {{ userInitials }}
              </div>
              <span class="text-gray-700 hidden md:inline">{{ userName }}</span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-4 w-4 text-gray-500"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M19 9l-7 7-7-7"
                />
              </svg>
            </button>
            <transition
              enter-active-class="transition ease-out duration-100"
              enter-from-class="transform opacity-0 scale-95"
              enter-to-class="transform opacity-100 scale-100"
              leave-active-class="transition ease-in duration-75"
              leave-from-class="transform opacity-100 scale-100"
              leave-to-class="transform opacity-0 scale-95"
            >
              <div
                v-if="showDropdown"
                class="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-1 z-50 ring-1 ring-black ring-opacity-5"
              >
                <a
                  href="#"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-purple-600"
                  >Your Profile</a
                >
                <a
                  href="#"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-purple-600"
                  >Settings</a
                >
                <a
                  href="#"
                  @click="logout"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-purple-600"
                  >Sign out</a
                >
              </div>
            </transition>
          </div>
        </div>
      </div>
    </nav>

    <!-- Main Dashboard Content -->
    <div class="container mx-auto px-4 py-6">
      <div class="flex flex-col lg:flex-row gap-6">
        <!-- Sidebar -->
        <div class="lg:w-64 flex-shrink-0">
          <div class="bg-white rounded-lg shadow-sm p-4 sticky top-20">
            <div class="space-y-1">
              <button
                v-for="tab in tabs"
                :key="tab.id"
                @click="navigateTo(tab)"
                :class="[
                  activeTab === tab.id
                    ? 'bg-purple-50 text-purple-600 border-l-4 border-purple-600'
                    : 'text-gray-700 hover:bg-gray-50',
                  'w-full text-left px-4 py-3 rounded-md flex items-center transition-colors duration-150',
                ]"
                aria-label="Navigate to dashboard section"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 mr-3"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    :d="tab.icon"
                  />
                </svg>
                {{ tab.label }}
                <span
                  v-if="tab.notification"
                  class="ml-auto bg-purple-100 text-purple-800 text-xs px-2 py-0.5 rounded-full"
                >
                  {{ tab.notification }}
                </span>
              </button>
            </div>

            <!-- Mood Quick Log -->
            <div class="mt-8">
              <h3
                class="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-3"
              >
                Quick Mood Check-In
              </h3>
              <div class="grid grid-cols-5 gap-2">
                <button
                  v-for="mood in moods"
                  :key="mood.id"
                  @click="logMood(mood.id)"
                  :class="[
                    selectedMood === mood.id
                      ? 'bg-purple-100 ring-2 ring-purple-300'
                      : 'hover:bg-gray-50',
                    'p-2 rounded-full flex flex-col items-center transition-all duration-200',
                  ]"
                  :aria-label="`Log ${mood.label} mood`"
                >
                  <span class="text-2xl">{{ mood.emoji }}</span>
                  <span class="text-xs mt-1 text-gray-600">{{
                    mood.label
                  }}</span>
                </button>
              </div>
            </div>

            <!-- Daily Affirmation -->
            <div class="mt-8 p-4 bg-purple-50 rounded-lg">
              <h3 class="text-sm font-medium text-purple-800 mb-2">
                Today's Affirmation
              </h3>
              <p class="text-xs text-gray-700 italic">
                "I am capable of handling whatever comes my way today."
              </p>
            </div>
          </div>
        </div>

        <!-- Main Content Area -->
        <div class="flex-1">
          <!-- Welcome Card -->
          <div
            class="bg-gradient-to-r from-purple-500 to-purple-600 text-white rounded-xl shadow-md p-6 mb-6"
          >
            <div
              class="flex flex-col md:flex-row md:items-center md:justify-between"
            >
              <div>
                <h2 class="text-xl font-bold mb-1">
                  Welcome back, {{ userName }}!
                </h2>
                <p class="mb-4 opacity-90">How are you feeling today?</p>
              </div>
              <button
                @click="startChat"
                class="bg-white text-purple-600 px-4 py-2 rounded-lg font-medium hover:bg-gray-50 transition-colors shadow-sm self-start md:self-auto"
              >
                Chat with FikraTech
              </button>
            </div>
          </div>

          <!-- Dashboard Stats -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <div
              class="bg-white p-4 rounded-lg shadow-sm border-l-4 border-purple-500"
            >
              <h3 class="text-sm font-medium text-gray-500 mb-1">
                Current Streak
              </h3>
              <p class="text-2xl font-bold text-gray-900">5 days</p>
            </div>
            <div
              class="bg-white p-4 rounded-lg shadow-sm border-l-4 border-blue-500"
            >
              <h3 class="text-sm font-medium text-gray-500 mb-1">
                Journal Entries
              </h3>
              <p class="text-2xl font-bold text-gray-900">12</p>
            </div>
            <div
              class="bg-white p-4 rounded-lg shadow-sm border-l-4 border-green-500"
            >
              <h3 class="text-sm font-medium text-gray-500 mb-1">
                Mood Average
              </h3>
              <p class="text-2xl font-bold text-gray-900">7.2/10</p>
            </div>
          </div>

          <!-- Mood Tracker Card -->
          <div class="bg-white rounded-xl shadow-sm p-6 mb-6">
            <div
              class="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-4"
            >
              <h3 class="text-lg font-semibold text-gray-900 mb-2 sm:mb-0">
                Your Mood This Week
              </h3>
              <div class="flex space-x-2">
                <button
                  class="text-sm px-3 py-1 bg-purple-50 text-purple-600 rounded-md"
                >
                  Week
                </button>
                <button
                  class="text-sm px-3 py-1 text-gray-500 hover:bg-gray-50 rounded-md"
                >
                  Month
                </button>
                <button
                  class="text-sm px-3 py-1 text-gray-500 hover:bg-gray-50 rounded-md"
                >
                  Year
                </button>
              </div>
            </div>
            <div class="h-64">
              <!-- Mood chart placeholder with improved visualization -->
              <div class="h-full flex flex-col">
                <div class="flex-1 grid grid-cols-7 gap-2">
                  <div
                    v-for="day in moodData"
                    :key="day.id"
                    class="flex flex-col items-center justify-end"
                  >
                    <div
                      :class="[
                        'w-full rounded-t-sm',
                        day.value >= 8
                          ? 'bg-green-400'
                          : day.value >= 6
                          ? 'bg-blue-400'
                          : day.value >= 4
                          ? 'bg-yellow-400'
                          : 'bg-red-400',
                      ]"
                      :style="{ height: `${day.value * 10}%` }"
                    ></div>
                    <span class="text-xs text-gray-500 mt-1">{{
                      day.day
                    }}</span>
                  </div>
                </div>
                <div
                  class="flex justify-between text-xs text-gray-500 mt-2 px-2"
                >
                  <span>Mon</span>
                  <span>Tue</span>
                  <span>Wed</span>
                  <span>Thu</span>
                  <span>Fri</span>
                  <span>Sat</span>
                  <span>Sun</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Journal and AI Assistant Section -->
          <div class="grid md:grid-cols-2 gap-6 mb-6">
            <!-- Journal Card -->
            <div class="bg-white rounded-xl shadow-sm p-6">
              <div class="flex items-center justify-between mb-4">
                <h3 class="text-lg font-semibold text-gray-900">
                  Recent Journal Entries
                </h3>
                <button
                  @click="startJournal"
                  class="text-sm flex items-center text-purple-600 hover:text-purple-700"
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
                      d="M12 4v16m8-8H4"
                    />
                  </svg>
                  New Entry
                </button>
              </div>
              <div class="space-y-4">
                <div
                  v-for="entry in journalEntries"
                  :key="entry.id"
                  class="group p-3 hover:bg-gray-50 rounded-lg transition-colors cursor-pointer"
                >
                  <div class="flex items-start">
                    <div
                      class="flex-shrink-0 h-10 w-10 bg-purple-50 rounded-lg flex items-center justify-center text-purple-600 mr-3"
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="h-5 w-5"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                        />
                      </svg>
                    </div>
                    <div class="flex-1 min-w-0">
                      <h4 class="text-sm font-medium text-gray-900 truncate">
                        {{ entry.title }}
                      </h4>
                      <p class="text-sm text-gray-500 mt-1">
                        {{ entry.preview }}
                      </p>
                      <div class="mt-2 flex items-center text-xs text-gray-400">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          class="h-3 w-3 mr-1"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                        >
                          <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                          />
                        </svg>
                        {{ entry.date }}
                      </div>
                    </div>
                  </div>
                </div>
                <div
                  v-if="journalEntries.length === 0"
                  class="text-center py-8"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-12 w-12 mx-auto text-gray-300"
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
                  <p class="mt-2 text-gray-500">No journal entries yet</p>
                  <button
                    @click="startJournal"
                    class="mt-3 text-sm font-medium text-purple-600 hover:text-purple-700 inline-flex items-center"
                  >
                    Start your first entry
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-4 w-4 ml-1"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M14 5l7 7m0 0l-7 7m7-7H3"
                      />
                    </svg>
                  </button>
                </div>
              </div>
            </div>

            <!-- AI Assistant Card -->
            <div class="bg-white rounded-xl shadow-sm p-6">
              <div class="flex items-center mb-4">
                <div
                  class="flex-shrink-0 h-10 w-10 bg-purple-100 rounded-lg flex items-center justify-center text-purple-600 mr-3"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
                    />
                  </svg>
                </div>
                <h3 class="text-lg font-semibold text-gray-900">
                  FikraTech Assistant
                </h3>
              </div>

              <div class="space-y-4">
                <div class="bg-gray-50 rounded-lg p-4">
                  <div class="flex items-start mb-3">
                    <div
                      class="flex-shrink-0 h-8 w-8 bg-purple-100 rounded-full flex items-center justify-center text-purple-600 mr-2"
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="h-4 w-4"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
                        />
                      </svg>
                    </div>
                    <p class="text-sm text-gray-800">
                      Hi {{ userName }}, I noticed you haven't checked in today.
                      Would you like to share how you're feeling?
                    </p>
                  </div>

                  <div class="flex mt-4">
                    <input
                      type="text"
                      placeholder="Type your response..."
                      class="flex-grow border border-gray-300 rounded-l-lg px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                    />
                    <button
                      class="bg-purple-600 text-white px-4 py-2 rounded-r-lg hover:bg-purple-700 text-sm font-medium transition-colors"
                    >
                      Send
                    </button>
                  </div>
                </div>

                <div class="grid grid-cols-2 gap-2">
                  <button
                    v-for="prompt in quickPrompts"
                    :key="prompt.id"
                    @click="selectPrompt(prompt)"
                    class="text-xs text-left p-2 bg-gray-50 hover:bg-gray-100 rounded-lg transition-colors"
                  >
                    {{ prompt.text }}
                  </button>
                </div>
              </div>
            </div>
          </div>

          <!-- Resources Section -->
          <div class="bg-white rounded-xl shadow-sm p-6">
            <div class="flex items-center justify-between mb-4">
              <h3 class="text-lg font-semibold text-gray-900">
                Recommended For You
              </h3>
              <a href="#" class="text-sm text-purple-600 hover:text-purple-700"
                >View all</a
              >
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div
                v-for="resource in resources"
                :key="resource.id"
                class="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow cursor-pointer"
              >
                <div class="flex items-center mb-3">
                  <div
                    :class="[
                      'flex-shrink-0 h-10 w-10 rounded-lg flex items-center justify-center mr-3',
                      resource.type === 'article'
                        ? 'bg-blue-100 text-blue-600'
                        : resource.type === 'meditation'
                        ? 'bg-purple-100 text-purple-600'
                        : 'bg-green-100 text-green-600',
                    ]"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-5 w-5"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        v-if="resource.type === 'article'"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
                      />
                      <path
                        v-if="resource.type === 'meditation'"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
                      />
                      <path
                        v-if="resource.type === 'exercise'"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M13 10V3L4 14h7v7l9-11h-7z"
                      />
                    </svg>
                  </div>
                  <div>
                    <span
                      class="text-xs font-medium px-2 py-1 rounded-full"
                      :class="[
                        resource.type === 'article'
                          ? 'bg-blue-50 text-blue-600'
                          : resource.type === 'meditation'
                          ? 'bg-purple-50 text-purple-600'
                          : 'bg-green-50 text-green-600',
                      ]"
                    >
                      {{ resource.type }}
                    </span>
                  </div>
                </div>
                <h4 class="font-medium text-gray-900 mb-1">
                  {{ resource.title }}
                </h4>
                <p class="text-sm text-gray-600 mb-3">
                  {{ resource.description }}
                </p>
                <div class="flex items-center text-xs text-gray-500">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-3 w-3 mr-1"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                  {{ resource.duration }} min read
                </div>
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

// User data
const userName = ref("Zaineb");
const userInitials = ref("Z");
const showDropdown = ref(false);
const selectedMood = ref(null);

// Dashboard tabs
const tabs = ref([
  {
    id: "dashboard",
    label: "Dashboard",
    icon: "M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6",
    notification: null,
  },
  {
    id: "journal",
    label: "Journal",
    icon: "M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z",
    path: "/journal",
    notification: 2,
  },
  {
    id: "mood",
    label: "Mood Tracker",
    icon: "M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z",
    path: "/dashboard/MoodTracker",
    notification: null,
  },
  {
    id: "resources",
    label: "Resources",
    icon: "M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253",
    path: "/resources",
    notification: 5,
  },
  {
    id: "community",
    label: "Community",
    icon: "M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z",
    path: "/community",
    notification: null,
  },
]);

const activeTab = ref("dashboard");

// Mood tracking
const moods = ref([
  { id: 1, emoji: "😊", label: "Happy" },
  { id: 2, emoji: "😐", label: "Neutral" },
  { id: 3, emoji: "😔", label: "Sad" },
  { id: 4, emoji: "😰", label: "Anxious" },
  { id: 5, emoji: "😡", label: "Angry" },
]);

// Mood data for chart
const moodData = ref([
  { id: 1, day: "M", value: 7 },
  { id: 2, day: "T", value: 8 },
  { id: 3, day: "W", value: 6 },
  { id: 4, day: "T", value: 5 },
  { id: 5, day: "F", value: 4 },
  { id: 6, day: "S", value: 8 },
  { id: 7, day: "S", value: 9 },
]);

// Journal entries
const journalEntries = ref([
  {
    id: 1,
    title: "Morning Reflection",
    preview:
      "Today I woke up feeling refreshed and ready to take on the day...",
    date: "2 hours ago",
  },
  {
    id: 2,
    title: "Work Stress",
    preview:
      "The project deadline is approaching and I feel the pressure building up...",
    date: "Yesterday",
  },
  {
    id: 3,
    title: "Gratitude Entry",
    preview:
      "I am grateful for my supportive friends who checked in on me today...",
    date: "2 days ago",
  },
]);

// AI Assistant quick prompts
const quickPrompts = ref([
  { id: 1, text: "I'm feeling anxious about..." },
  { id: 2, text: "What coping strategies do you recommend?" },
  { id: 3, text: "I need help relaxing" },
  { id: 4, text: "Suggest a mindfulness exercise" },
]);

// Resources
const resources = ref([
  {
    id: 1,
    title: "Managing Anxiety",
    description: "Practical techniques to help reduce anxiety in daily life",
    type: "article",
    duration: 5,
    link: "#",
  },
  {
    id: 2,
    title: "Sleep Meditation",
    description: "Guided meditation for better sleep quality",
    type: "meditation",
    duration: 10,
    link: "#",
  },
  {
    id: 3,
    title: "5-Minute Breathing",
    description: "Quick exercises to calm your mind",
    type: "exercise",
    duration: 5,
    link: "#",
  },
]);

// Methods
const toggleUserDropdown = () => {
  showDropdown.value = !showDropdown.value;
};

const logout = () => {
  router.push("/index");
};

const showNotificationDropdown = ref(false);
const unreadNotifications = ref(true);
const lastNotificationTime = ref(new Date());
const positiveMessages = ref([
  "You're doing great! Keep up the positive energy!",
  "Remember to take breaks and practice self-care today.",
  "Your progress is amazing! Celebrate small wins.",
  "You have the power to make today wonderful!",
  "Just a reminder: You're stronger than you think.",
]);

// Format time for display
const formatTime = (date) => {
  return date.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
};

// Show notifications dropdown
const showNotifications = () => {
  showNotificationDropdown.value = !showNotificationDropdown.value;
  if (showNotificationDropdown.value) {
    unreadNotifications.value = false;
  }
};

// Check every 5 hours for new notifications
onMounted(() => {
  setInterval(() => {
    unreadNotifications.value = true;
    lastNotificationTime.value = new Date();
  }, 5 * 60 * 60 * 1000); // 5 hours in milliseconds
});

const logMood = (moodId) => {
  selectedMood.value = moodId;
  alert(`Logged mood: ${moods.value.find((m) => m.id === moodId).label}`);
  // In a real app, this would send the mood data to your backend
};

const startChat = () => {
  alert("Starting chat with AI assistant...");
};

const startJournal = () => {
  alert("Opening journal entry...");
};

const selectPrompt = (prompt) => {
  alert(`Selected prompt: "${prompt.text}"`);
};
</script>

<style>
/* Custom styles */
body {
  @apply antialiased text-gray-800;
}

/* Smooth transitions for interactive elements */
button,
a {
  @apply transition-colors duration-200;
}

/* Focus styles for accessibility */
button:focus,
input:focus {
  @apply outline-none ring-2 ring-purple-500 ring-opacity-50;
}
</style>
