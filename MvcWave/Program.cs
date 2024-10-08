using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using Npgsql.EntityFrameworkCore.PostgreSQL;
using Npgsql;
using NpgsqlTypes;
using MvcWave.Data;
using MvcMovie.Data;
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddDbContext<MvcRoadKContext>(options =>
    options.UseNpgsql(builder.Configuration.GetConnectionString("MvcRoadKContext") ?? throw new InvalidOperationException("Connection string 'MvcRoadKContext' not found.")));


if (builder.Environment.IsDevelopment()){
    builder.Services.AddDbContext<MvcWaveContext>(options =>

        options.UseNpgsql(builder.Configuration.GetConnectionString("ProductionMvcWaveContext")));
        //options.UseSqlite(builder.Configuration.GetConnectionString("MvcWaveContext")));
}

else{    
    builder.Services.AddDbContext<MvcWaveContext>(options =>
        options.UseNpgsql(builder.Configuration.GetConnectionString("ProductionMvcWaveContext")));

        //sqllite for dev, postgres for prod
}

// Add services to the container.
builder.Services.AddControllersWithViews();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();
