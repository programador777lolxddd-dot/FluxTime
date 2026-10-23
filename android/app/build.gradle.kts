plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "dev.fluxtime.clock"
    compileSdk = 35

    defaultConfig {
        applicationId = "dev.fluxtime.clock"
        minSdk = 23
        targetSdk = 35
        versionCode = 1
        versionName = "0.1.0"
    }
}
