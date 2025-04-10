<template>
  <div class="min-h-screen bg-white">
    <!-- Navigation -->
    <nav class="bg-gradient-to-r from-blue-50 to-purple-50 shadow-sm">
      <div
        class="container mx-auto px-4 py-4 flex justify-between items-center"
      >
        <div class="flex items-center">
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
          <div class="ml-2">
            <h1 class="text-xl font-bold text-gray-800">FekraTech</h1>
            <p class="text-xs text-gray-500">AI for Mental Wellness</p>
          </div>
        </div>
        <div class="hidden md:flex space-x-8">
          <a href="#about-us" class="text-gray-600 hover:text-purple-600"
            >About Us</a
          >
          <a href="#our-team" class="text-gray-600 hover:text-purple-600"
            >Our Team</a
          >
          <a href="#our-services" class="text-gray-600 hover:text-purple-600"
            >Features</a
          >
          <a href="#how-it-works" class="text-gray-600 hover:text-purple-600"
            >How It Works</a
          >
        </div>
        <div class="flex items-center space-x-4">
          <button
            @click="navigateToLogin"
            class="px-4 py-2 text-gray-600 hover:text-purple-600"
          >
            Log In
          </button>
          <button
            @click="navigateToLogin"
            class="px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition-colors"
          >
            Sign Up
          </button>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <section
      class="relative bg-gradient-to-r from-blue-50 to-purple-50 py-32 overflow-hidden"
    >
      <div
        class="container mx-auto px-4 flex flex-col items-center text-center"
      >
        <h1
          class="text-4xl md:text-5xl font-bold text-gray-900 mb-6 leading-tight"
        >
          Your mental wellness journey starts here
        </h1>

        <!-- AI-generated quote -->
        <div class="max-w-2xl mb-8">
          <blockquote
            class="text-xl md:text-2xl font-light text-gray-700 italic mb-6"
          >
            "Be kind to your mind. Your mental health is just as important as
            your physical health."
          </blockquote>
        </div>

        <!-- Action buttons -->
        <div class="flex flex-col sm:flex-row gap-4">
          <button
            @click="navigateToLogin"
            class="bg-gradient-to-r from-purple-500 to-purple-600 text-white font-bold px-6 py-3 rounded-lg hover:from-purple-600 hover:to-purple-700 transition-all shadow-md"
          >
            Try Now
          </button>
          <button
            @click="scrollToExplainer"
            class="bg-white text-gray-800 font-bold px-6 py-3 rounded-lg border border-gray-300 hover:bg-gray-50 transition-colors shadow-sm"
          >
            How It Works
          </button>
        </div>
      </div>
    </section>

    <!-- About Us Section -->
    <section id="about-us" class="py-16 bg-white">
      <div class="container mx-auto px-4">
        <div class="text-center mb-12">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
            About Us
          </h2>
          <div class="flex justify-center">
            <p class="text-gray-600 max-w-2xl mx-auto text-lg">
              FekraTech is an AI-powered platform created by tech enthusiasts to
              make mental health support more accessible and stigma-free. By
              leveraging our expertise in artificial intelligence, we generate
              personalized text, images, and audio content that promotes mental
              wellness through positive, engaging interactions. Our tool
              complements professional care by providing 24/7 support and
              encouraging healthy habits – helping users take the first step
              toward emotional wellbeing in a comfortable, judgment-free space.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Our Team Section -->
    <section id="our-team" class="py-16 bg-gray-50">
      <div class="container mx-auto px-4">
        <div class="text-center mb-12">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            Our Team
          </h2>
          <p class="text-xl text-gray-600 max-w-3xl mx-auto">
            The passionate students behind FekraTech
          </p>
        </div>

        <div class="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
          <div class="bg-white p-8 rounded-xl shadow-sm text-center">
            <div
              class="w-32 h-32 rounded-full bg-purple-100 mx-auto mb-4 flex items-center justify-center"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-16 w-16 text-purple-600"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="1.5"
                  d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                />
              </svg>
            </div>
            <h3 class="text-xl font-bold text-gray-800 mb-2">Zaineb</h3>
            <p class="text-purple-600 mb-2">AI Research Student</p>
            <p class="text-gray-600">
              Focused on developing our machine learning models with a special
              interest in emotional recognition algorithms.
            </p>
          </div>

          <div class="bg-white p-8 rounded-xl shadow-sm text-center">
            <div
              class="w-32 h-32 rounded-full bg-purple-100 mx-auto mb-4 flex items-center justify-center"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-16 w-16 text-purple-600"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="1.5"
                  d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                />
              </svg>
            </div>
            <h3 class="text-xl font-bold text-gray-800 mb-2">Islem</h3>
            <p class="text-purple-600 mb-2">AI Development Student</p>
            <p class="text-gray-600">
              Specializes in implementing our AI solutions with clean, efficient
              code and user-friendly interfaces.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Our Services Section -->
    <section id="our-services" class="py-16 bg-white">
      <div class="container mx-auto px-4">
        <div class="text-center mb-12">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            Our Wellness Features
          </h2>
          <p class="text-xl text-gray-600 max-w-3xl mx-auto">
            Tools to support your mental health journey
          </p>
        </div>

        <div class="grid md:grid-cols-3 gap-8">
          <div class="bg-purple-50 p-8 rounded-xl border border-purple-100">
            <div
              class="w-16 h-16 bg-purple-100 rounded-lg flex items-center justify-center text-purple-600 mb-6"
            >
              <svg
                class="w-8 h-8"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
                ></path>
              </svg>
            </div>
            <h3 class="text-xl font-bold text-gray-800 mb-3">Mood Tracker</h3>
            <p class="text-gray-600">
              Monitor your emotional patterns with insightful analytics and
              personalized recommendations.
            </p>
            <button
              @click="navigateToMoodTracker"
              class="mt-4 text-purple-600 hover:text-purple-800 font-medium"
            >
              Start Tracking
            </button>
          </div>

          <div class="bg-purple-50 p-8 rounded-xl border border-purple-100">
            <div
              class="w-16 h-16 bg-purple-100 rounded-lg flex items-center justify-center text-purple-600 mb-6"
            >
              <svg
                class="w-8 h-8"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3"
                ></path>
              </svg>
            </div>
            <h3 class="text-xl font-bold text-gray-800 mb-3">
              Relaxation Music
            </h3>
            <p class="text-gray-600">
              Curated audio experiences to help you unwind, focus, or sleep
              better.
            </p>
            <button
              @click="navigateToMoodTracker"
              class="mt-4 text-purple-600 hover:text-purple-800 font-medium"
            >
              Listen Now
            </button>
          </div>

          <div class="bg-purple-50 p-8 rounded-xl border border-purple-100">
            <div
              class="w-16 h-16 bg-purple-100 rounded-lg flex items-center justify-center text-purple-600 mb-6"
            >
              <svg
                class="w-8 h-8"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"
                ></path>
              </svg>
            </div>
            <h3 class="text-xl font-bold text-gray-800 mb-3">
              Positive Messages
            </h3>
            <p class="text-gray-600">
              Daily affirmations and encouraging notifications tailored to your
              needs.
            </p>
            <button
              @click="startMessages"
              class="mt-4 text-purple-600 hover:text-purple-800 font-medium"
            >
              Get Inspired
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- 3-Step Explainer Section -->
    <section id="how-it-works" class="py-16 bg-gray-50">
      <div class="container mx-auto px-4">
        <h2
          class="text-3xl md:text-4xl font-bold text-center text-gray-900 mb-12"
        >
          How It Works
        </h2>

        <div class="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
          <!-- Step 1 -->
          <div
            class="text-center p-8 rounded-xl bg-white border border-gray-100 shadow-sm hover:shadow-md transition-shadow"
          >
            <div
              class="w-20 h-20 bg-purple-100 rounded-full flex items-center justify-center text-purple-600 text-2xl font-bold mx-auto mb-4"
            >
              1
            </div>
            <h3 class="text-xl font-bold mb-3 text-gray-800">Sign Up</h3>
            <p class="text-gray-600">
              Create your free account to personalize your wellness experience.
            </p>
          </div>

          <!-- Step 2 -->
          <div
            class="text-center p-8 rounded-xl bg-white border border-gray-100 shadow-sm hover:shadow-md transition-shadow"
          >
            <div
              class="w-20 h-20 bg-purple-100 rounded-full flex items-center justify-center text-purple-600 text-2xl font-bold mx-auto mb-4"
            >
              2
            </div>
            <h3 class="text-xl font-bold mb-3 text-gray-800">Explore</h3>
            <p class="text-gray-600">
              Discover tools that match your needs and preferences.
            </p>
          </div>

          <!-- Step 3 -->
          <div
            class="text-center p-8 rounded-xl bg-white border border-gray-100 shadow-sm hover:shadow-md transition-shadow"
          >
            <div
              class="w-20 h-20 bg-purple-100 rounded-full flex items-center justify-center text-purple-600 text-2xl font-bold mx-auto mb-4"
            >
              3
            </div>
            <h3 class="text-xl font-bold mb-3 text-gray-800">Feel Better</h3>
            <p class="text-gray-600">
              Build healthy habits with our daily wellness tools.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Future Features Section -->
    <section id="future-features" class="py-16 bg-white">
      <div class="container mx-auto px-4 text-center">
        <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
          Coming Soon
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto mb-12">
          Exciting new features we're working on
        </p>

        <div class="grid md:grid-cols-2 lg:grid-cols-2 gap-8 max-w-4xl mx-auto">
          <div
            class="bg-white p-8 rounded-xl shadow-sm border border-gray-100 opacity-75"
          >
            <div
              class="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center text-gray-400 mb-6 mx-auto"
            >
              <svg
                class="w-8 h-8"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"
                ></path>
              </svg>
            </div>
            <h3 class="text-xl font-bold mb-3 text-gray-800">
              AI Chat Companion
            </h3>
            <p class="text-gray-600 mb-4">
              An empathetic conversation partner available 24/7
            </p>
            <span class="text-sm text-purple-600 font-medium">Coming Soon</span>
          </div>

          <div
            class="bg-white p-8 rounded-xl shadow-sm border border-gray-100 opacity-75"
          >
            <div
              class="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center text-gray-400 mb-6 mx-auto"
            >
              <svg
                class="w-8 h-8"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"
                ></path>
              </svg>
            </div>
            <h3 class="text-xl font-bold mb-3 text-gray-800">
              Therapist Connect
            </h3>
            <p class="text-gray-600 mb-4">
              Professional support when you need it most
            </p>
            <span class="text-sm text-purple-600 font-medium">Coming Soon</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials -->
    <section id="testimonials" class="py-16 bg-gray-50">
      <div class="container mx-auto px-4">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            What Our Community Says
          </h2>
          <p class="text-xl text-gray-600 max-w-3xl mx-auto">
            Real stories from people who've used FekraTech to support their
            mental health.
          </p>
        </div>

        <div class="grid md:grid-cols-3 gap-8">
          <div class="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
            <div class="flex items-center mb-4">
              <div
                class="w-12 h-12 rounded-full bg-gray-200 flex items-center justify-center text-gray-500 font-bold mr-4"
              >
                MM
              </div>
              <div>
                <h4 class="font-bold text-gray-800">Mariem M.</h4>
                <p class="text-sm text-gray-500">College Student</p>
              </div>
            </div>
            <p class="text-gray-600 italic">
              "The mood tracker helped me understand my stress patterns better
              than anything else I've tried."
            </p>
            <div class="mt-4 flex text-yellow-400">
              <span>★</span>
              <span>★</span>
              <span>★</span>
              <span>★</span>
              <span class="text-gray-300">★</span>
            </div>
          </div>

          <div class="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
            <div class="flex items-center mb-4">
              <div
                class="w-12 h-12 rounded-full bg-gray-200 flex items-center justify-center text-gray-500 font-bold mr-4"
              >
                SM
              </div>
              <div>
                <h4 class="font-bold text-gray-800">Sarah M.</h4>
                <p class="text-sm text-gray-500">Graphic Designer</p>
              </div>
            </div>
            <p class="text-gray-600 italic">
              "The relaxation music helps me focus during work and unwind at the
              end of the day."
            </p>
            <div class="mt-4 flex text-yellow-400">
              <span>★</span>
              <span>★</span>
              <span>★</span>
              <span class="text-gray-300">★</span>
              <span class="text-gray-300">★</span>
            </div>
          </div>

          <div class="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
            <div class="flex items-center mb-4">
              <div
                class="w-12 h-12 rounded-full bg-gray-200 flex items-center justify-center text-gray-500 font-bold mr-4"
              >
                TP
              </div>
              <div>
                <h4 class="font-bold text-gray-800">Thomas P.</h4>
                <p class="text-sm text-gray-500">Software Engineer</p>
              </div>
            </div>
            <p class="text-gray-600 italic">
              "The daily positive messages give me a much-needed boost during
              stressful workdays."
            </p>
            <div class="mt-4 flex text-yellow-400">
              <span>★</span>
              <span>★</span>
              <span>★</span>
              <span>★</span>
              <span>★</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Final CTA -->
    <section
      class="py-20 bg-gradient-to-r from-purple-500 to-purple-600 text-white"
    >
      <div class="container mx-auto px-4 text-center">
        <h2 class="text-3xl md:text-4xl font-bold mb-6">
          Start Your Mental Wellness Journey Today
        </h2>
        <p class="text-xl mb-8 max-w-2xl mx-auto opacity-90">
          Join thousands who are using FekraTech to support their emotional
          well-being.
        </p>
        <div class="flex flex-col sm:flex-row justify-center gap-4">
          <button
            @click="navigateToLogin"
            class="px-8 py-4 bg-white text-purple-600 font-bold rounded-lg hover:bg-gray-100 transition-colors shadow-lg hover:shadow-xl"
          >
            Sign Up Free
          </button>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

// Navigation functions
const navigateToMoodTracker = () => {
  router.push("/dashboard/MoodTracker");
};

const scrollToExplainer = () => {
  const element = document.getElementById("how-it-works");
  element?.scrollIntoView({ behavior: "smooth" });
};

const navigateToLogin = () => {
  router.push("/login");
};

const navigateToDashboard = () => {
  router.push("/dashboard/home-dashboard");
};

const startMessages = () => {
  alert("Positive messages would appear here");
};

// Initialize
onMounted(() => {
  // Any initialization code
});
</script>

<style>
/* Custom animations */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Smooth scrolling */
html {
  scroll-behavior: smooth;
}
</style>
