package com.smartlockinc.smartlocks;

        import android.app.Activity;
        import android.content.Context;
        import android.content.Intent;
        import android.graphics.Color;
        import android.os.AsyncTask;
        import android.os.Bundle;
        import android.support.design.widget.TabLayout;
        import android.support.v4.view.ViewPager;
        import android.support.v4.widget.DrawerLayout;
        import android.support.v7.app.ActionBarActivity;
        import android.support.v7.widget.Toolbar;
        import android.util.Log;
        import android.view.Menu;
        import android.view.MenuItem;
        import android.view.View;
        import android.widget.TextView;
        import android.widget.Toast;

        import com.alexzh.circleimageview.CircleImageView;
        import com.alexzh.circleimageview.ItemSelectedListener;
        import com.android.volley.Request;
        import com.android.volley.RequestQueue;
        import com.android.volley.Response;
        import com.android.volley.VolleyError;
        import com.android.volley.toolbox.JsonObjectRequest;
        import com.android.volley.toolbox.Volley;
        import com.google.android.gms.gcm.GoogleCloudMessaging;
        import com.squareup.picasso.Picasso;

        import org.json.JSONException;
        import org.json.JSONObject;

        import java.io.IOException;

        import static com.smartlockinc.smartlocks.CommonUtilities.SENDER_ID;


public class rooms extends Activity {

    AsyncTask<Void, Void, Void> mRegisterTask;
    AlertDialogueManager alert = new AlertDialogueManager();
    ConnectionDetector cd;
    SessionManager session;
    Gcmsessionmanager gcmsessionmanager;
    private NavigationDrawerFragment mNavigationDrawerFragment;
    private Toolbar mToolbar;
    private PagerAdapter madapter;
    LoginDataBaseAdapter loginDataBaseAdapter;
    GoogleCloudMessaging gcm;
    photourl uri;
    TextView usrname;
    TextView name;
    CircleImageView img;
    TabLayout mtablayout;
    ViewPager pager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.rooms);
        Intent intent = getIntent();
    }

    public void bedroom1(View v1) {
        RequestQueue rq = Volley.newRequestQueue(this);
        JSONObject jsonObject = new JSONObject();

        try {
            jsonObject.put("keyword", "1");
        } catch (JSONException e) {
            e.printStackTrace();
        }

        JsonObjectRequest postReq = new JsonObjectRequest(Request.Method.POST, "http://192.168.43.147:5000/smartlock/led3/action", jsonObject, new Response.Listener<JSONObject>() {

            @Override
            public void onResponse(JSONObject response) {

                try {
                    String data = response.getString("success");

                } catch (JSONException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }


            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                System.out.println("Error [" + error + "]");

            }
        }); /*{
                @Override

                protected Map<String, String> getParams() {
                    Map<String, String> params = new HashMap<String, String>();
                    params.put("keyword",keyword);
                    return params;
                }


            };*/

        rq.add(postReq);

    }

    public void bedroom2(View v1) {
        RequestQueue rq = Volley.newRequestQueue(this);
        JSONObject jsonObject = new JSONObject();
        try {
            jsonObject.put("keyword", "1");
        } catch (JSONException e) {
            e.printStackTrace();
        }

        JsonObjectRequest postReq = new JsonObjectRequest(Request.Method.POST, "http://192.168.43.147:5000/smartlock/led4/action", jsonObject, new Response.Listener<JSONObject>() {

            @Override
            public void onResponse(JSONObject response) {

                try {
                    String data = response.getString("success");

                } catch (JSONException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }


            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                System.out.println("Error [" + error + "]");

            }
        }); /*{
                @Override

                protected Map<String, String> getParams() {
                    Map<String, String> params = new HashMap<String, String>();
                    params.put("keyword",keyword);
                    return params;
                }


            };*/

        rq.add(postReq);

    }

    public void kitchen(View v1) {
        RequestQueue rq = Volley.newRequestQueue(this);
        JSONObject jsonObject = new JSONObject();
        try {
            jsonObject.put("keyword", "1");
        } catch (JSONException e) {
            e.printStackTrace();
        }

        JsonObjectRequest postReq = new JsonObjectRequest(Request.Method.POST, "http://192.168.43.147:5000/smartlock/led2/action", jsonObject, new Response.Listener<JSONObject>() {

            @Override
            public void onResponse(JSONObject response) {

                try {
                    String data = response.getString("success");

                } catch (JSONException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }


            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                System.out.println("Error [" + error + "]");

            }
        }); /*{
                @Override

                protected Map<String, String> getParams() {
                    Map<String, String> params = new HashMap<String, String>();
                    params.put("keyword",keyword);
                    return params;
                }


            };*/

        rq.add(postReq);

    }

    public void diningroom(View v1) {
        RequestQueue rq = Volley.newRequestQueue(this);
        JSONObject jsonObject = new JSONObject();
        try {
            jsonObject.put("keyword", "1");
        } catch (JSONException e) {
            e.printStackTrace();
        }

        JsonObjectRequest postReq = new JsonObjectRequest(Request.Method.POST, "http://192.168.43.147:5000/smartlock/led5/action", jsonObject, new Response.Listener<JSONObject>() {

            @Override
            public void onResponse(JSONObject response) {

                try {
                    String data = response.getString("success");

                } catch (JSONException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }


            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                System.out.println("Error [" + error + "]");

            }
        }); /*{
                @Override

                protected Map<String, String> getParams() {
                    Map<String, String> params = new HashMap<String, String>();
                    params.put("keyword",keyword);
                    return params;
                }


            };*/

        rq.add(postReq);

    }

    public void livingroom(View v1) {
        RequestQueue rq = Volley.newRequestQueue(this);
        JSONObject jsonObject = new JSONObject();
        try {
            jsonObject.put("keyword", "1");
        } catch (JSONException e) {
            e.printStackTrace();
        }

        JsonObjectRequest postReq = new JsonObjectRequest(Request.Method.POST, "http://192.168.43.147:5000/smartlock/led1/action", jsonObject, new Response.Listener<JSONObject>() {

            @Override
            public void onResponse(JSONObject response) {

                try {
                    String data = response.getString("success");

                } catch (JSONException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }


            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                System.out.println("Error [" + error + "]");

            }
        }); /*{
                @Override

                protected Map<String, String> getParams() {
                    Map<String, String> params = new HashMap<String, String>();
                    params.put("keyword",keyword);
                    return params;
                }


            };*/

        rq.add(postReq);

    }










}



