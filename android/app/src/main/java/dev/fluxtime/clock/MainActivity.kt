package dev.fluxtime.clock

import android.app.Activity
import android.graphics.Color
import android.graphics.Typeface
import android.os.Bundle
import android.view.Gravity
import android.view.View
import android.widget.LinearLayout
import android.widget.TextView
import android.os.Handler
import android.os.Looper
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

class MainActivity : Activity() {
    private val handler = Handler(Looper.getMainLooper())
    private lateinit var clockText: TextView
    private lateinit var dateText: TextView
    private val cyan = Color.rgb(0, 240, 255)
    private val pink = Color.rgb(255, 0, 128)
    private val purple = Color.rgb(180, 100, 255)
    private val slate = Color.rgb(120, 120, 160)

    private val ticker = object : Runnable {
        override fun run() {
            val now = Date()
            clockText.text = SimpleDateFormat("HH:mm:ss", Locale.getDefault()).format(now)
            dateText.text = SimpleDateFormat("EEEE, d 'de' MMMM 'de' yyyy", Locale("es", "ES"))
                .format(now).replaceFirstChar { if (it.isLowerCase()) it.titlecase(Locale("es", "ES")) else it.toString() }
            handler.postDelayed(this, 250L)
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        window.statusBarColor = Color.rgb(10, 2, 20)
        window.navigationBarColor = Color.rgb(10, 2, 20)
        window.decorView.systemUiVisibility = View.SYSTEM_UI_FLAG_LOW_PROFILE

        val root = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            gravity = Gravity.CENTER
            setPadding(18, 24, 18, 24)
            setBackgroundColor(Color.rgb(10, 2, 20))
        }

        val banner = TextView(this).apply {
            text = "███████╗\n██╔════╝\n█████╗  \n██╔══╝  \n██║     \n╚══════╝"
            typeface = Typeface.MONOSPACE
            textSize = 16f
            setTextColor(pink)
            gravity = Gravity.CENTER
        }

        val brand = TextView(this).apply {
            text = "MIDNIGHT PLASMA"
            typeface = Typeface.create("sans-serif-medium", Typeface.BOLD)
            textSize = 14f
            letterSpacing = 0.18f
            setTextColor(purple)
            gravity = Gravity.CENTER
        }

        clockText = TextView(this).apply {
            typeface = Typeface.MONOSPACE
            textSize = 38f
            setTextColor(cyan)
            gravity = Gravity.CENTER
            includeFontPadding = false
        }

        dateText = TextView(this).apply {
            typeface = Typeface.create("sans-serif", Typeface.NORMAL)
            textSize = 14f
            setTextColor(purple)
            gravity = Gravity.CENTER
        }

        val footer = TextView(this).apply {
            text = "FluxTime • la hora, en modo terminal"
            typeface = Typeface.MONOSPACE
            textSize = 10f
            setTextColor(slate)
            gravity = Gravity.CENTER
        }

        root.addView(banner, LinearLayout.LayoutParams(-1, -2).apply { bottomMargin = 14 })
        root.addView(brand, LinearLayout.LayoutParams(-1, -2).apply { bottomMargin = 28 })
        root.addView(clockText, LinearLayout.LayoutParams(-1, -2).apply { bottomMargin = 16 })
        root.addView(dateText, LinearLayout.LayoutParams(-1, -2).apply { bottomMargin = 32 })
        root.addView(footer, LinearLayout.LayoutParams(-1, -2))
        setContentView(root)
        handler.post(ticker)
    }

    override fun onDestroy() {
        handler.removeCallbacks(ticker)
        super.onDestroy()
    }
}
